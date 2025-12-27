# Minesweeper
This project is a recreation of the classic Minesweeper game. The code and assets were written and drawn from scratch.

<img src="https://github.com/Ayk-12/minesweeper/blob/main/Screenshots/minesweeper-empty.png" width="50%" height="50%"/>

Running the main file (*minesweeper.py*) should open a window with the board.
If the "pygame" package is not installed, the program will not run. Download it using `pip install pygame`.

## Gameplay

Left click on a tile to uncover it. Right click on a tile to mark/unmark it as safe. The number on the top left corner represents the number of bombs left (starts at 118 and decreases with each tile flagged). The number on the top right represents the elapsed time since the beginning of the round.

Clicking on the smiley face on the top resets the board. The game finishes when all bombs are flagged correctly (not when all safe tiles are opened).

The game starts with a single green tile. It is encouraged to start from there, as it is guaranteed that the green tile is safe.

<img src="https://github.com/Ayk-12/minesweeper/blob/main/Screenshots/minesweeper-start.png" width="50%" height="50%"/>
