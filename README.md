# Simple Snake Game (Python + Turtle)

This is a simple Snake game built with Python's `turtle` module, created as a learning project. The snake moves on a 2D grid, eats food to grow, and the game tracks both your current score and a persistent high score.

## Features

- Classic Snake gameplay using the keyboard arrow keys.
- Food appears at random positions within the window.
- Score increases whenever the snake eats food.
- High score is saved and loaded from `highscore.txt` between runs.
- Collision detection with walls and the snake's own body.
- Implemented using only the Python standard library (`turtle`, `random`).

## Requirements

- Python 3.8 or later.
- A desktop environment that can open a `turtle` graphics window (Windows, macOS, or Linux).

No external dependencies are required.

## Installation

```bash
git clone https://github.com/chaitanyaCE/Simple_Snake_Game.git
cd Simple_Snake_Game
```

(Optional) Create and activate a virtual environment:

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS / Linux
source .venv/bin/activate
```

There is no `requirements.txt` because the project only uses the standard library.

## Running the Game

The main entry point of the project is `final_project.py` [file:13].

```bash
python final_project.py
```

Make sure you run this command from the project root (the same folder where `final_project.py` is located).

## How to Play

- Use the **arrow keys**:
  - Up arrow: move up.
  - Down arrow: move down.
  - Left arrow: move left.
  - Right arrow: move right.
- Eat the food (a circle drawn with `turtle`) to grow and increase your score.
- Avoid:
  - Hitting the window borders.
  - Colliding with your own body.
- When you collide with a wall or yourself:
  - The game calls `reset()` and restarts with score reset to 0.
  - The high score (stored in `highscore.txt`) is preserved and updated if you beat it [file:13].

## Project Structure

Core learning steps are broken into multiple files, plus a final version of the game:

- `starter.py` – Initial setup and very basic snake drawing (intro step) [file:18].
- `basic_snake_movement.py` – Basic movement of the snake using `turtle` and keyboard controls [file:12].
- `sontrolling_snake_direction.py` – Functions for changing snake direction with key bindings [file:16].
- `snake_food.py` – Adds random food spawning and simple food collision [file:17].
- `score_keeping.py` – Adds a score variable and displays score in the window title [file:14].
- `collisions_detection.py` – Handles collision with walls and self, ending the game when a collision happens [file:11].
- `reset_game.py` – Introduces full reset logic for restarting the game when a collision occurs [file:15].
- `final_project.py` – The **complete** Snake game:
  - Uses direction binding with `binddirectionkeys`.
  - Tracks score and high score, storing the high score in `highscore.txt`.
  - Handles collisions and automatically resets the game on collision [file:13].

You can open each intermediate file to see how the game evolves step by step.

## High Score File

The file `final_project.py` reads and writes a `highscore.txt` file in the same directory to store the high score between runs [file:13].

- If `highscore.txt` does not exist, the game starts with a high score of 0 and creates the file when you beat it.
- Make sure you have write permissions in the project directory so the file can be created/updated.

## Customization Ideas

- Change `WIDTH`, `HEIGHT`, `DELAY`, `FOODSIZE`, or `SNAKESIZE` constants in `final_project.py` to adjust game speed and difficulty [file:13].
- Change colors (background, snake, food) by editing the relevant `turtle` settings (e.g., `screen.bgcolor`, `stamper.color`).
- Add a pause key, difficulty levels, or a start menu using more key bindings and states.

## Contributing

This project is mainly for learning, but improvements are welcome:

1. Fork the repository.
2. Create a feature branch: `git checkout -b feature/my-change`.
3. Commit your changes: `git commit -m "Describe my change"`.
4. Push the branch: `git push origin feature/my-change`.
5. Open a pull request.

## License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.
