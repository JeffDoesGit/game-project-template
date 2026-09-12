# ENGINE.md — Unreal Engine {{ENGINE_VERSION}}

## Setup (P0-1, via Claude Code on the machine with the engine installed)
1. Find the engine: `%PROGRAMDATA%\Epic\UnrealEngineLauncher\LauncherInstalled.dat` → InstallLocation for {{ENGINE_VERSION}}. Report it. Do not assume `C:\Program Files\Epic Games`.
2. Toolchain: MSVC + Windows SDK inside the range in `<Engine>/Engine/Config/Windows/Windows_SDK.json`. The MSVC folder name is a family label; UBT reads the real compiler version. Verify with a build, not by reading folder names.
3. Build from the command line first, never from the editor prompt:
   `"<Engine>\Engine\Build\BatchFiles\Build.bat" <Project>Editor Win64 Development -Project="<full path>.uproject" -WaitMutex`
   Baseline on `main` must be 0 warnings, 0 errors before any change.
4. Commit `.uproject`, `Config/`, `Source/`, `Content/`. Never `Binaries/`, `Intermediate/`, `Saved/`, `DerivedDataCache/`.

## Language and layout
- C++ for systems; Blueprints for content wiring only. Data Assets and Data Tables for all balance.
- `Source/<Project>/<System>/` one folder per system. `Content/<Project>/` for first-party; `Content/<Pack>/` for third-party.
- Naming prefixes: `BP_ WBP_ M_ MI_ T_ SM_ SK_ AM_ ABP_ DA_ DT_ NS_ ST_ IA_ IMC_`. Third-party packs keep theirs.
- Tick is opt-in and justified in the PR (CLAUDE.md 5.3).

## Assets and LFS
`.gitattributes`: `*.uasset *.umap *.png *.fbx *.wav` → LFS, lockable. Lock before editing a shared binary.

## CI
GitHub-hosted runners **cannot build Unreal** (no engine, ~14 GB disk). `tier1` is engine-free; a compile check needs a self-hosted runner on a machine with the engine — only ever on a private repo (CLAUDE.md 7.3). Decide the build host as a `D-` memo when "green CI over a broken main" first costs a day.

## Dev tooling
`FAutoConsoleCommand` under `#if !UE_BUILD_SHIPPING`. Never a design rule.
