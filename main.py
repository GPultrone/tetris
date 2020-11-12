import pygame
from tetris import Tetris

wScreen = 500
hScreen = 1000

if __name__ == '__main__':
    pygame.init()
    win = pygame.display.set_mode((wScreen, hScreen))
    pygame.display.set_caption('Tetris')

    tetris = Tetris(win, wScreen, hScreen)

    pygame.quit()