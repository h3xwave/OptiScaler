# Translation maintenance

Edit the tracked Python dictionaries (`tr_data_*.py`), not just `lang/zh-CN.txt`.
Recent upstream menu additions are in `tr_data_menu.py`; later dictionaries
override earlier ones as defined by `merged_table()`.

```powershell
python scripts/i18n/merge_all_translations.py --write
python scripts/i18n/validate_translations.py
python scripts/i18n/merge_all_translations.py --check
python scripts/i18n/check_menu_coverage.py
python -m unittest discover -s scripts/i18n -p "test_*.py"
# Windows + MSVC: exercise actual ImGui text output with Release optimizations
python scripts/i18n/test_imgui_release.py
```

The generator normalizes ordering/comments. Its semantic check compares keys,
values and printf signatures rather than requiring a byte-identical file.

## Coverage boundary

`check_menu_coverage.py` checks literal arguments to its listed ImGui/helper
functions, sidebar/card tables, MenuOption labels/descriptions/disabled reasons,
Keybind labels, and the literal choices in `QuirksTabLabel`.
It handles comments, adjacent literals and hidden widget IDs. Each intentionally
untranslated technical identifier needs a reason in `coverage_allowlist.json`.
Do not add ordinary UI prose to that list just to make CI pass.

This is a lexical check, not a C++ compiler or complete UI coverage proof.
Variable-built strings, arbitrary option arrays and other source files still
need review and in-game testing. ImGui text and widget translation is compiled
into the function bodies: do not revert it to runtime Detours, which inlining
can bypass. A translated format string does not translate its `%s` arguments;
use `ShowTooltip()`/`TextUnformatted()` for descriptions and translate each part
before composing restart notices or other dynamic text. Whenever a new helper renders
user-visible text, extend the extractor and add a regression test.

## Release checks

The unsigned Windows build runs tests and all validators, checking each native
exit code immediately. Upstream sync explicitly dispatches both that build and
clang-format; every `gh` command targets `--repo "$GITHUB_REPOSITORY"` so the CLI
cannot resolve the official upstream instead of this fork. The sync workflow
needs `contents: write`, `pull-requests: write` and `actions: write`.

Repository settings must allow Actions to create PRs and enable **Allow auto-merge**.
Keep `master` protected with the GitHub Actions `build` and `Formatting Check`
checks required, branches required to be up to date, and no administrator bypass.
The scheduled/manual sync stages `upstream-sync-candidate`, dispatches CI, creates
or reuses its PR, then requests auto-merge for that exact head commit. It uses a
merge commit to preserve upstream ancestry and all fork-specific commits; it never
force-pushes `master`. Merge conflicts stop the workflow, while failed or pending
checks keep the PR unmerged. New upstream UI strings can require additions to the
tracked dictionaries and language pack before the translation checks will pass.
Dispatching a workflow or enabling auto-merge alone does not prove CI passed.

Before release, test sidebar labels, status tables, custom tabs and font rendering
in games using DX11, DX12 and Vulkan. Font-library smoke tests are not a substitute
for game integration tests.
