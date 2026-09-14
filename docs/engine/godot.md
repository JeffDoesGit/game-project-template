# ENGINE.md — Godot

## Setup (P0-1, via Claude Code on the machine with Godot installed)
1. Confirm `godot --version` matches {{ENGINE_VERSION}}. Report the path.
2. `godot --headless --path . --editor --quit` once to generate `.godot/` and import; confirm exit code 0.
3. Commit `project.godot`, `icon.svg`, `export_presets.cfg` if present. Never commit `.godot/`.

## Language and layout
- GDScript unless `GDD.md` 9.x says C#. Static typing on every declaration (`var x: int`, `func f() -> void`).
- `scenes/` (one folder per feature, scene + script together) · `scripts/` (autoloads, shared) · `data/` (`.tres` resources — all balance lives here) · `assets/` (art, audio, fonts; third-party packs in `assets/thirdparty/<pack>/`) · `tests/` (GUT or gdUnit4).
- Naming: scenes `snake_case.tscn`, scripts `snake_case.gd`, classes `PascalCase` via `class_name`, resources `snake_case.tres`, nodes `PascalCase`.
- Signals over polling; `_process` is opt-in and justified in the PR (CLAUDE.md 5.3).

## Assets and LFS
`.gitattributes`: `*.png *.jpg *.wav *.ogg *.mp3 *.ttf *.otf *.glb *.gltf *.blend` → LFS. `.tres`/`.tscn` are text and are not.

## CI
Godot runs headless on GitHub-hosted runners for free, so a **compile-and-test check is possible from day one**: `tier1` can run `godot --headless --path . --check-only` on every script and the test suite. Wire it in P0-2. Cache the editor binary; use the official `godot-ci` container or download the release zip.

## Dev tooling
Debug overlays behind `OS.is_debug_build()`. Console commands via an autoload gated the same way.
