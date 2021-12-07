

GRID = [[0, 0, 9, 0, 8, 5, 0, 0, 0],
        [0, 6, 0, 0, 0, 0, 0, 0, 9],
        [0, 7, 8, 0, 0, 0, 0, 1, 4],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 5, 0, 1, 8, 0, 0, 0],
        [0, 0, 0, 7, 0, 0, 4, 8, 2],
        [0, 0, 0, 0, 0, 7, 0, 4, 0],
        [2, 0, 0, 6, 0, 9, 0, 0, 0],
        [0, 8, 0, 0, 0, 0, 0, 7, 0]]

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

def get_pos():
    for i, row in enumerate(GRID):
        for j, num in enumerate(row):
            if num == 0:
                return (i, j)
    return None

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

def main():
    fill()
    print(GRID)
