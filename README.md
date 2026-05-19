# Asteroids (Course Project)

A small Asteroids-style game built with Python and pygame.

## Project Scope

This game is intentionally basic. I implemented what was required for the course, and I do not plan to further improve this kind of visual game.

I am blind, so this project was completed to satisfy the coursework requirements rather than as a long-term game development focus.

## Requirements

- Python 3.13+
- pygame 2.6.1

## Install

If you are using uv:

```bash
uv sync
```

Or with pip:

```bash
python -m pip install pygame==2.6.1
```

## Run

```bash
python main.py
```

## Controls

- W: move forward
- S: move backward
- A: rotate left
- D: rotate right
- Space: shoot
- Close window: quit

## Logging

The game writes lightweight JSONL logs while running:

- game_state.jsonl: periodic state snapshots
- game_events.jsonl: event records (hits, shots, splits)

## Repository Layout

- main.py: game loop and setup
- player.py: player movement and shooting
- asteroid.py: asteroid behavior and splitting
- asteroidfield.py: timed asteroid spawning
- shot.py: projectile behavior
- circleshape.py: shared collision base class
- constants.py: gameplay constants
- logger.py: JSONL state/event logging
