# AI Lab 2 — Smart Classroom Agent

## Files

- `lab2_percept.py`: Reflex agent; chooses a target mode from the current percept.
- `lab2_model.py`: Stateful agent; remembers the previous target mode and avoids repeated commands.
- `lab2_check.py`: Runs checks for thresholds, repeated percepts, mode changes, boundaries, and empty-room priority.

## Requirements

Python 3. No third-party packages are needed.

## Run

Open a terminal in this folder and run:

```bash
python lab2_percepts.py
python lab2_model.py
python lab2_check.py
```

## Policy

- If the room is empty, target mode is `ECO`.
- If occupied and temperature is above 26°C, target mode is `COOL`.
- If occupied and temperature is below 20°C, target mode is `WARM`.
- Otherwise, target mode is `IDLE`.
- At exactly 20°C and 26°C, an occupied room uses `IDLE`.
- The stateful agent sends a command only if its target differs from the previous target. On its first action, the previous mode is `None`, so it sends the first command.

The modes are simulated labels; this code does not control real classroom hardware.
