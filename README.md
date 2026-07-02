# Asteroids (Course Project)

A small Asteroids-style game built with Python and pygame.

## Project Scope

This game is intentionally basic. I implemented what was required for the
course, and I do not plan to further improve this kind of visual game.

I am blind, so this project was completed to satisfy the coursework requirements
rather than as a long-term game development focus.

## Quick Start

If you are using uv:

```bash
uv sync
python main.py
```

Or with pip:

```bash
python -m pip install pygame==2.6.1
python main.py
```

## Requirements

- Python 3.13+
- pygame 2.6.1

## Gameplay

This is an endless survival loop:

- Asteroids spawn over time.
- You move and rotate the ship to avoid collisions.
- Shooting large asteroids splits them into smaller ones.
- The run ends immediately when the player collides with an asteroid.

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

Both files contain timestamped entries. `game_state.jsonl` samples runtime state
roughly once per second, and `game_events.jsonl` logs one entry per gameplay
event.

## Troubleshooting

- If pygame install fails, make sure you are using a supported Python version
  (3.13+ in this project).
- If the window opens and closes immediately, run from a terminal to see printed
  startup output and errors.
- If controls do not respond, click the game window once to ensure it has
  keyboard focus.

## Contributing

- Contribution guide: [CONTRIBUTING.md](CONTRIBUTING.md)
- Development notes: [DEVELOPMENT.md](DEVELOPMENT.md)

## Repository Layout

- main.py: game loop and setup
- player.py: player movement and shooting
- asteroid.py: asteroid behavior and splitting
- asteroidfield.py: timed asteroid spawning
- shot.py: projectile behavior
- circleshape.py: shared collision base class
- constants.py: gameplay constants
- logger.py: JSONL state/event logging
