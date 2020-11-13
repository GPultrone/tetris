import pygame
from tetris import Tetris

wScreen = 400
hScreen = 800
wWindow = 500
hWindow = 1000

if __name__ == '__main__':
    pygame.init()
    win = pygame.display.set_mode((wWindow, hWindow))
    pygame.display.set_caption('Tetris')

    tetris = Tetris(win, wScreen, hScreen, wWindow, hWindow)

    pygame.quit()