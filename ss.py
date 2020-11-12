import pygame
from sprite import Sprite

class Ss(Sprite):
    def __init__(self, x, y, win, wScreen, hScreen):
        super(Ss, self).__init__(x, y, win, wScreen, hScreen)
        self.width = 35
        self.height = 54
        self.ss = pygame.image.load('sprite/VA.png')

        self.scale()

    def scale(self):
        newWidth = (self.wScreen/10)*2
        newHeight = (self.hScreen/20)*3
        self.ss = pygame.transform.scale(self.ss, (round(newWidth), round(newHeight)))

    def draw(self):
        self.win.blit(self.ss, (self.x, self.y))