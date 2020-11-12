import pygame
from sprite import Sprite

class Linea(Sprite):
    def __init__(self, x, y, win, wScreen, hScreen):
        super(Linea, self).__init__(x, y, win, wScreen, hScreen)
        self.width = 18
        self.height = 72
        self.linea = pygame.image.load('sprite/A.png')

        self.scale()

    def scale(self):
        newWidth = (self.wScreen/10)
        newHeight = (self.hScreen/20)*4
        self.linea = pygame.transform.scale(self.linea, (round(newWidth), round(newHeight)))

    def draw(self):
        self.win.blit(self.linea, (self.x, self.y))