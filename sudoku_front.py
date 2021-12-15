import pygame, sys
from pygame.locals import *
from sudoku_solve import *
from time import sleep
from Button import Button

pygame.init()

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
GREY = (220, 220, 220)
RED = (255, 0, 0)

button_fast = Button(WHITE, 90, 520, 150, 50, text='fast algorithm')
button_visual = Button(WHITE, 250, 520, 150, 50, text='visualize algorithm')
text_solving = font2.render('Solving in progress...', 1, (255, 0, 0))

def message_to_screen(msg, color, position, Font):
    text = Font.render(msg, True, color)
    screen.blit(text, position)

def draw_lines():
    for i in range(1, 10):
        if i == 3 or i == 6:
            pygame.draw.line(screen, BLACK, (0, i * SQUARE), (WIDTH, i * SQUARE), 5)
            pygame.draw.line(screen, BLACK, (i*SQUARE, 0), (i * SQUARE, SQUARE * 9), 5)
        else:
            pygame.draw.line(screen, BLACK, (0, i * SQUARE), (WIDTH, i * SQUARE))
            pygame.draw.line(screen, BLACK, (i*SQUARE, 0), (i * SQUARE, SQUARE * 9))

    for i, row in enumerate(GRID):
        for j, num in enumerate(row):
            if num != 0:
                message_to_screen(str(num), BLACK, (j * SQUARE + 20, i * SQUARE + 15), Font)

def fill_pg():
    sleep(0.25)
    screen.fill(GREY)
    draw_lines()
    pos = get_pos()
    if not pos:
        return True
    else:
        i, j = pos
    for n in range(1, 10):
        if check(n, pos) == True:
            GRID[i][j] = n
            screen.fill(GREY)
            draw_lines()
            message_to_screen(str(n), BLACK, (j * SQUARE + 20, i * SQUARE + 15), Font)
            pygame.draw.rect(screen, GREEN, [j * SQUARE, i * SQUARE, SQUARE, SQUARE], width=4 )
            pygame.display.update()
            if fill_pg():
                return True
            GRID[i][j] = 0
            screen.fill(GREY)
            draw_lines()
            message_to_screen("0", BLACK, (j * SQUARE + 20, i * SQUARE + 15), Font)
            pygame.display.update()
    return False


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
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
                print(int(rect_y / SQUARE))
                print(int(rect_x / SQUARE))
                GRID[int(rect_y / SQUARE)][int(rect_x / SQUARE)] = 0
            if event.key == K_1 or event.key == K_2 or event.key == K_3 or event.key == K_4 or event.key == K_5 or event.key == K_6 or event.key == K_7 or event.key == K_8 or event.key == K_9:
                GRID[int(rect_y / SQUARE)][int(rect_x / SQUARE)] = int(event.unicode)
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if button_visual.is_under(pos):
                pygame.display.update()
                fill_pg()
            if button_fast.is_under(pos):
                screen.blit(text_solving, (35, 200))
                pygame.display.update()
                fill()


    screen.fill(GREY)
    button_fast.draw(screen)
    button_visual.draw(screen)
    draw_lines()
    pygame.draw.rect(screen, BLACK, [rect_x, rect_y, SQUARE, SQUARE], width=4 )
    pygame.display.update()
