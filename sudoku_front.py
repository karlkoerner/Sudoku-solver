import pygame, sys
from pygame.locals import *
from sudoku_solve import *
from time import sleep
from Button import Button

pygame.init()

# PYGAME VARIABLES
WIDTH, HEIGHT = 495, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
SQUARE = 55
Font = pygame.font.SysFont('comicsans', 45)
font2 = pygame.font.SysFont('comicsans', 60)
rect_x = 55
rect_y = 55
BLACK = (0, 0, 0)
GREEN = (100, 255, 100)
WHITE = (255, 255, 255)
LIGHT_GREY = (220, 220, 220)
DARK_GREY = (100, 100, 100)
RED = (255, 0, 0)
SPEED = 0.25

button_fast = Button(WHITE, 90, 520, 150, 50, text='fast algorithm')
button_visual = Button(WHITE, 250, 520, 150, 50, text='visualize algorithm')
text_solving = font2.render('Solving in progress...', 1, (255, 0, 0))

# prints a text (input) in a given color, font and position (input) to the screen
def message_to_screen(msg, color, position, Font):
    text = Font.render(msg, True, color)
    screen.blit(text, position)

# creates a list with the positions of all the numbers, of the original sudoku
def set_default():
    default = []
    for i, line in enumerate(GRID):
        for j, num in enumerate(line):
            if num != 0:
                default.append((i, j))
    return default

# sets the value of the numbers that are not in the default list to 0 (so the algorithm can work)
def clear(default):
    for i, row in enumerate(GRID):
        for j, num in enumerate(row):
            if (i, j) not in default:
                GRID[i][j] = 0

# draws the GRID and the numbers in it
def draw_GRID():
    # draws the lines (makes every third line a thick line)
    for i in range(1, 10):
        if i == 3 or i == 6:
            pygame.draw.line(screen, BLACK, (0, i * SQUARE), (WIDTH, i * SQUARE), 5)
            pygame.draw.line(screen, BLACK, (i*SQUARE, 0), (i * SQUARE, SQUARE * 9), 5)
        else:
            pygame.draw.line(screen, BLACK, (0, i * SQUARE), (WIDTH, i * SQUARE))
            pygame.draw.line(screen, BLACK, (i*SQUARE, 0), (i * SQUARE, SQUARE * 9))
    # displays the numbers to the screen
    for i, row in enumerate(GRID):
        for j, num in enumerate(row):
            if num != 0:
                if (i, j) in default:
                    message_to_screen(str(num), BLACK, (j * SQUARE + 5, i * SQUARE), Font)
                else:
                    message_to_screen(str(num), DARK_GREY, (j * SQUARE + 5, i * SQUARE), Font)

# represents the same functionality as the "fill()" function from sudoku_solve but visualizes every step and draws it to the screen
def fill_pg():
    sleep(SPEED)
    screen.fill(LIGHT_GREY)
    draw_GRID()
    pos = get_pos()
    if not pos:
        return True
    else:
        i, j = pos
        GRID[i][j] = 0
    for n in range(1, 10):
        if check(n, pos) == True:
            GRID[i][j] = n
            screen.fill(LIGHT_GREY)
            draw_GRID()
            message_to_screen(str(n), BLACK, (j * SQUARE + 5, i * SQUARE), Font)
            pygame.draw.rect(screen, GREEN, [j * SQUARE, i * SQUARE, SQUARE, SQUARE], width=4 )
            pygame.display.update()
            if fill_pg():
                return True
            GRID[i][j] = 0
            screen.fill(LIGHT_GREY)
            draw_GRID()
            message_to_screen("0", BLACK, (j * SQUARE + 5, i * SQUARE), Font)
            pygame.draw.rect(screen, RED, [j * SQUARE, i * SQUARE, SQUARE, SQUARE], width=4 )
            sleep(SPEED)
            pygame.display.update()
    return False


# MAIN LOOP
default = set_default()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Button functionality --> move the square around the screen, delete a number, place a new number
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if rect_x >= SQUARE:
                    rect_x -= SQUARE
            if event.key == pygame.K_RIGHT:
                if rect_x <= WIDTH - 2*SQUARE:
                    rect_x += SQUARE
            if event.key == pygame.K_UP:
                if rect_y >= SQUARE:
                    rect_y -= SQUARE
            if event.key == pygame.K_DOWN:
                if rect_y <= WIDTH - 2*SQUARE:
                    rect_y += SQUARE
            if event.key == pygame.K_BACKSPACE:
                GRID[int(rect_y / SQUARE)][int(rect_x / SQUARE)] = 0
            if event.key == K_1 or event.key == K_2 or event.key == K_3 or event.key == K_4 or event.key == K_5 or event.key == K_6 or event.key == K_7 or event.key == K_8 or event.key == K_9:
                if (int(rect_y / SQUARE), int(rect_x / SQUARE)) not in default:
                # ^^^ This if-statement takes care that the original numbers of the sudoku can not be changed.
                    GRID[int(rect_y / SQUARE)][int(rect_x / SQUARE)] = int(event.unicode)

        # starts an algorithm by detecting a clicked Button
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if button_visual.is_under(pos):
                pygame.display.update()
                clear(default)
                fill_pg()
            if button_fast.is_under(pos):
                screen.blit(text_solving, (35, 200))
                pygame.display.update()
                clear(default)
                fill()


    screen.fill(LIGHT_GREY)
    button_fast.draw(screen)
    button_visual.draw(screen)
    draw_GRID()
    pygame.draw.rect(screen, BLACK, [rect_x, rect_y, SQUARE, SQUARE], width=4 )
    pygame.display.update()
