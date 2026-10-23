# Bundled FreeType

Version: **2.13.3**, matching the public headers already bundled here.
Source: https://github.com/freetype/freetype, tag `VER-2-13-3`, commit
`42608f77f20749dd6ddc9e0536788eaad70ea4b5`. No FreeType source patches.

## Runtime libraries

- `freetype.lib`: x64 Release, DLL CRT (`/MD`). Used by Release and ReleaseDebug.
- `freetyped.lib`: x64 Debug, debug DLL CRT (`/MDd`). Used by Debug.

Both are **static FreeType libraries**; only their C runtime is dynamically linked.
Do not mix the former `/MT` library with OptiScaler's `/MD` objects or suppress
LNK4098 instead of correcting the mismatch.

The build uses FreeType's internal zlib. Optional external bzip2, PNG, HarfBuzz
and Brotli dependencies are disabled, matching the bundled `ftoption.h`.

## Rebuild

Requires Git, Visual Studio 2022 C++ tools and CMake 3.24+ (bundled with recent
VS 2022 installations, or `cmake` on PATH):

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/deps/rebuild_freetype.ps1
```

The script checks out the pinned source, builds both configurations outside the
source tree under ignored `artifacts/` (refreshing the CMake cache), checks
archive CRT directives, and only
then replaces the bundled libraries. `-SourceDir`, `-BuildRoot`, and `-CMake`
can select an existing clean pinned checkout and custom tool/build paths.
Build outputs need not be byte-identical across MSVC versions.

## License

FreeType is distributed under the FreeType License (FTL) for this bundle.
See `LICENSE.TXT` and `FTL.TXT`; both are copied into the Release package's
`Licenses` directory. Portions of this software are copyright © 2024
The FreeType Project (www.freetype.org). All rights reserved.
