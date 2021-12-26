# Sudoku-solver
## Sudoku solver using a backtracking algorithm (GUI with PyGame)

- move around using arrow keys
- type a number --> will be placed on the box surrounded by the thick, black square
- just override a number by typing in another one on the same box
- hit backspace to completely delete a number

There are two possibilities to solve the sudoku:
1. The fast algorithm just doeas the work on the backand and prints out the result in the end (much faster)
2. The visualized algorithm prints every step of the recursive function to the screen (speed can be changed in the Code by changing the SPEED variable)
   --> very slow especially when solving dificult sudokus
