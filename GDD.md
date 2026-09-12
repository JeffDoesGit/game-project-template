# {{GAME_NAME}} — Game Design Document

**Version:** 0.1
**Engine:** {{ENGINE}} {{ENGINE_VERSION}}
**Status:** Draft. The bootstrap hands off to the game project only when every rule the proof-of-concept slice needs is `DECIDED`.

## Conventions

Every rule carries exactly one tag:

- `DECIDED` — settled; changes only via the decision log (§12) in the same PR.
- `OPEN` — needs a decision before anything depending on it is built. Sessions may ship a `PROVISIONAL` placeholder (CLAUDE.md 1.6) but never decide.
- `LATER` — deliberately out of scope for now.

Rules are numbered `<section>.<n>` and never renumbered; a retired rule keeps its number and gets the tag `RETIRED` with a log row.

## 0. Repository

0.1 `DECIDED` — Repository `{{REPO}}` is private.

## 1. Vision

1.1 `OPEN` — One-paragraph pitch: what the player does, why it is fun, what it feels like.
1.2 `OPEN` — Three pillars. Every later rule should serve at least one.
1.3 `OPEN` — Reference games and what is taken from each.
1.4 `OPEN` — What this game is *not*.

## 2. Proof-of-concept slice

The slice is the smallest playable thing that proves the core loop is fun. **Every rule the slice depends on must be `DECIDED` before handoff.**

2.1 `OPEN` — What the slice contains, as a list of nouns and verbs.
2.2 `OPEN` — The success test: what a playtester does, and what "it works" looks like.
2.3 `OPEN` — What is explicitly excluded from the slice.

## 3. Core loop

3.1 `OPEN` — The loop as a sequence: verb → verb → verb → repeat, with the reward at each step.
3.2 `OPEN` — Session length and what one session accomplishes.

## 4. Player

4.1 `OPEN` — Controls and input scheme.
4.2 `OPEN` — Movement model (speed, acceleration, jump, dash — numbers are `PROVISIONAL` until tuned; the *model* is decided here).
4.3 `OPEN` — Camera.
4.4 `OPEN` — Player stats and how they change.

## 5. Systems

One subsection per system the slice needs. Each system states: what it does, its inputs and outputs, what it depends on, and what is data vs code.

5.1 `OPEN` — 

## 6. Content

6.1 `OPEN` — Enemies / obstacles / NPCs in the slice, as a table with one row each.
6.2 `OPEN` — Levels / areas in the slice.
6.3 `OPEN` — Items / pickups / resources in the slice.

## 7. Progression

7.1 `OPEN` — What grows, how, and what it unlocks. `LATER` if the slice has none.

## 8. Presentation

8.1 `OPEN` — Art direction in three sentences, with references.
8.2 `OPEN` — Audio direction.
8.3 `OPEN` — UI: what is on screen during play.

## 9. Technical

9.1 `DECIDED` — Engine {{ENGINE}} {{ENGINE_VERSION}}, per `ENGINE.md`.
9.2 `OPEN` — Single-player only, local co-op, or networked. (Networked multiplies every later rule; decide it first.)
9.3 `OPEN` — Save model.
9.4 `OPEN` — Target platform(s) and performance floor.

## 10. Scope and schedule

10.1 `OPEN` — Slice target date.
10.2 `OPEN` — What comes after the slice, in order.

## 11. Open questions

A bulleted list of every `OPEN` rule above, maintained by the GDD chat. Empty at handoff for anything the slice needs.

## 12. Decision log

| Date | Rule(s) | Decision | Supersedes |
|---|---|---|---|
