import pygame
from sprite import Sprite

class Cubo(Sprite):
    def __init__(self, x, y, win, wScreen, hScreen):
        super(Cubo, self).__init__(x, y, win, wScreen, hScreen)
        self.width = 36
        self.height = 36
        self.cubo = pygame.image.load('sprite/V.png')

        self.scale()

    def scale(self):
        newWidth = (self.wScreen/10)*2
        newHeight = (self.hScreen/20)*2
        self.cubo = pygame.transform.scale(self.cubo, (round(newWidth), round(newHeight)))

    def draw(self):
        self.win.blit(self.cubo, (self.x, self.y))