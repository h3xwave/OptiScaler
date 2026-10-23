# Rebuild the bundled FreeType 2.13.3 for the DLL CRT used by OptiScaler.
# Run from any directory with PowerShell 5.1+; requires VS 2022 C++ tools and Git.
[CmdletBinding()]
param(
    [string] $SourceDir,
    [string] $BuildRoot,
    [string] $CMake
)

$ErrorActionPreference = 'Stop'
Set-StrictMode -Version Latest
$repo = [IO.Path]::GetFullPath((Join-Path $PSScriptRoot '..\..'))
$commit = '42608f77f20749dd6ddc9e0536788eaad70ea4b5'
$tag = 'VER-2-13-3'
if (-not $BuildRoot) { $BuildRoot = Join-Path $repo 'artifacts\freetype-2.13.3' }
$BuildRoot = [IO.Path]::GetFullPath($BuildRoot)

function Invoke-Checked([string] $Exe, [string[]] $Arguments) {
    # Windows PowerShell can turn native stderr warnings into terminating errors
    # when the caller redirects output. Native success is determined by exit code.
    $command = Get-Command $Exe -CommandType Application -ErrorAction Stop
    $previous = $ErrorActionPreference
    try {
        $ErrorActionPreference = 'Continue'
        & $command.Source @Arguments
        $code = $LASTEXITCODE
    }
    finally { $ErrorActionPreference = $previous }
    if ($code -ne 0) { throw "$Exe failed with exit code $code" }
}

$vswhere = Join-Path ${env:ProgramFiles(x86)} 'Microsoft Visual Studio\Installer\vswhere.exe'
$vs = & $vswhere -latest -version '[17.0,18.0)' -products '*' -requires Microsoft.VisualStudio.Component.VC.Tools.x86.x64 -property installationPath
if ($LASTEXITCODE -ne 0 -or -not $vs) { throw 'Visual Studio 2022 C++ tools are required' }
if (-not $CMake) {
    $CMake = Join-Path $vs 'Common7\IDE\CommonExtensions\Microsoft\CMake\CMake\bin\cmake.exe'
    if (-not (Test-Path $CMake)) { $CMake = (Get-Command cmake -ErrorAction Stop).Source }
}
$dumpbin = Get-ChildItem (Join-Path $vs 'VC\Tools\MSVC\*\bin\Hostx64\x64\dumpbin.exe') |
    Sort-Object FullName -Descending | Select-Object -First 1
if (-not $dumpbin) { throw 'dumpbin.exe was not found' }

if (-not $SourceDir) {
    $SourceDir = Join-Path $BuildRoot 'source'
    if (-not (Test-Path $SourceDir)) {
        New-Item -ItemType Directory -Force $BuildRoot | Out-Null
        Invoke-Checked git @('clone', '--depth', '1', '--branch', $tag,
            'https://github.com/freetype/freetype.git', $SourceDir)
    }
}
$SourceDir = [IO.Path]::GetFullPath($SourceDir)
$actual = & git -C $SourceDir rev-parse HEAD
if ($LASTEXITCODE -ne 0 -or $actual -ne $commit) { throw "Expected FreeType source commit $commit, got $actual" }
$dirty = & git -C $SourceDir status --porcelain
if ($LASTEXITCODE -ne 0 -or $dirty) { throw 'FreeType source must be a clean checkout' }

$build = Join-Path $BuildRoot 'build'
Invoke-Checked $CMake @('--fresh', '-S', $SourceDir, '-B', $build, '-G', 'Visual Studio 17 2022', '-A', 'x64', '-T', 'v143',
    "-DCMAKE_GENERATOR_INSTANCE=$vs", '-DCMAKE_POLICY_DEFAULT_CMP0091=NEW',
    '-DCMAKE_MSVC_RUNTIME_LIBRARY=MultiThreaded$<$<CONFIG:Debug>:Debug>DLL',
    '-DBUILD_SHARED_LIBS=OFF', '-DFT_DISABLE_ZLIB=ON', '-DFT_DISABLE_BZIP2=ON',
    '-DFT_DISABLE_PNG=ON', '-DFT_DISABLE_HARFBUZZ=ON', '-DFT_DISABLE_BROTLI=ON')

# Do not publish either library until BOTH configurations pass the CRT check.
foreach ($config in @('Release', 'Debug')) {
    Invoke-Checked $CMake @('--build', $build, '--config', $config, '--target', 'freetype', '--parallel')
    $name = if ($config -eq 'Debug') { 'freetyped.lib' } else { 'freetype.lib' }
    $library = Join-Path $build "$config\$name"
    if (-not (Test-Path $library)) { throw "Missing build output: $library" }
    $directives = & $dumpbin.FullName /nologo /directives $library
    if ($LASTEXITCODE -ne 0) { throw "Cannot inspect $library" }
    $directives = $directives -join "`n"
    $crt = if ($config -eq 'Debug') { 'MSVCRTD' } else { 'MSVCRT' }
    if ($directives -match '(?i)/DEFAULTLIB:"?LIBCMTD?\b' -or
        $directives -notmatch "(?i)/DEFAULTLIB:`"?$crt\b") {
        throw "Unexpected CRT in $library; expected $crt without LIBCMT"
    }
}

$destination = Join-Path $repo 'external\freetype'
Copy-Item (Join-Path $build 'Release\freetype.lib') $destination -Force
Copy-Item (Join-Path $build 'Debug\freetyped.lib') $destination -Force
Copy-Item (Join-Path $SourceDir 'LICENSE.TXT') $destination -Force
Copy-Item (Join-Path $SourceDir 'docs\FTL.TXT') $destination -Force
Write-Output 'FreeType Release (/MD) and Debug (/MDd) libraries rebuilt and checked.'
Get-FileHash (Join-Path $destination 'freetype.lib'), (Join-Path $destination 'freetyped.lib')
