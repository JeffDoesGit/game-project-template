# game-project-template

A repeatable starting point for a solo game project run with Claude: rules, design doc skeleton, roadmap protocol, decision memos, provisional register, and engine-free CI — the parts that caught real mistakes on the last project, without the parts that only existed because there was a team.

**Do not build a game in this repo.** Create a new repository from it (GitHub → *Use this template*, or the bootstrap chat does it), then replace every `{{PLACEHOLDER}}`.

## What's here

| Path | Purpose |
|---|---|
| `CLAUDE.md` | Binding rules for every session, human or AI. Engine-agnostic; engine specifics are in `docs/engine/`. |
| `GDD.md` | Design doc skeleton with the `DECIDED` / `OPEN` / `PROVISIONAL` convention and a decision log. **The bootstrap refuses to hand off until the proof-of-concept slice is fully `DECIDED`.** |
| `ROADMAP.md` | Session protocol (§1), STATUS block (§2), backlog (§3), phases (§4). |
| `docs/decisions/` | One memo per decision. `TEMPLATE.md` is the format. |
| `docs/provisional.md` | Register of every placeholder assumption in code. CI enforces parity. |
| `docs/systems/` | Plain-language page per implemented system. Generated wiki source. |
| `docs/devlog/` | One file per push-day. Player-facing summary + backlog x/y. |
| `docs/engine/` | Per-engine setup, folder layout, naming, CI notes. Bootstrap copies the right one to `ENGINE.md` and the right `.gitignore`. |
| `.github/workflows/tier1.yml` | Engine-free checks: provisional parity, roadmap hygiene. Required on `main`. |
| `claude-project/` | The new game's Claude project: instructions and the four chat prompts, with placeholders. |

## Placeholders

Written in files as `{{NAME}}`; listed here without braces so this line survives substitution:

`GAME_NAME` · `REPO` (owner/name) · `OWNER` · `ENGINE` (`godot` or `unreal`) · `ENGINE_VERSION` · `TOKEN_FILE`
