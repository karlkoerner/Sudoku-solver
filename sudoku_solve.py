
GRID = [[4, 1, 0, 0, 6, 0, 0, 7, 0],
        [0, 0, 3, 0, 8, 5, 0, 0, 9],
        [0, 2, 0, 3, 7, 0, 5, 0, 1],
        [8, 3, 0, 6, 0, 9, 2, 5, 0],
        [6, 0, 0, 5, 0, 1, 0, 0, 0],
        [5, 0, 9, 0, 2, 0, 0, 0, 3],
        [0, 0, 6, 2, 0, 0, 7, 4, 5],
        [1, 0, 0, 4, 9, 6, 8, 0, 0],
        [2, 8, 4, 0, 0, 0, 1, 9, 6]]

#returns True if a given number is repeated in the same row, column or square in the GRID
def check(num, pos):
    if num == 0:
        return False
    #check row
    for index, row in enumerate(GRID):
        for index0, n in enumerate(row):
            if pos[0] == index:
                if index0 != pos[1]:
                    if n == num:
                        return False
    #check column
    for index0, row in enumerate(GRID):
        for index, n in enumerate(row):
            if index == pos[1]:
                if index0 != pos[0]:
                    if num == n:
                        return False
    #check square
    y = pos[0] // 3
    x = pos[1] // 3
    for i in range(y*3, y*3 + 3):
        for j in range(x*3, x*3 + 3):
            if GRID[i][j] == num and (i,j) != pos:
                return False
    return True

#always returns the next empty position in the GRID
#--> if there is no empty position left it returns false => Sudoku solved
def get_pos():
    for i, row in enumerate(GRID):
        for j, num in enumerate(row):
            if num == 0:
                return (i, j)
    return None

#main solving recursive method:
# goes through grid and fills up every empty position (get_pos) if there is no possible solution for a digit from 1-9 to be filled in an empty position
# it goes back until is hits a previous position, where another solution is possible, then tries again from that position forward
# sudoku is solved, when there is no empty position left
def fill():
    pos = get_pos()
    if not pos:
        return True
    else:
        i, j = pos
    for n in range(1, 10):
        if check(n, pos) == True:
            GRID[i][j] = n

            if fill():
                return True
            GRID[i][j] = 0
    return False
