import pygame
from sprite import Sprite

class Sd(Sprite):
    def __init__(self, x, y, win, wScreen, hScreen):
        super(Sd, self).__init__(x, y, win, wScreen, hScreen)
        self.width = 35
        self.height = 54
        self.sd = pygame.image.load('sprite/RO.png')

        self.scale()

    def scale(self):
        newWidth = (self.wScreen/10)*2
        newHeight = (self.hScreen/20)*3
        self.sd = pygame.transform.scale(self.sd, (round(newWidth), round(newHeight)))

    def draw(self):
        self.win.blit(self.sd, (self.x, self.y))