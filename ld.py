import pygame
from sprite import Sprite

class Ld(Sprite):
    def __init__(self, x, y, win, wScreen, hScreen):
        super(Ld, self).__init__(x, y, win, wScreen, hScreen)
        self.width = 54
        self.height = 36
        self.ld = pygame.image.load('sprite/R.png')

        self.scale()

    def scale(self):
        newWidth = (self.wScreen/10)*3
        newHeight = (self.hScreen/20)*2
        self.ld = pygame.transform.scale(self.ld, (round(newWidth), round(newHeight)))

    def draw(self):
        self.win.blit(self.ld, (self.x, self.y))