import pygame
from sprite import Sprite

class T(Sprite):
    def __init__(self, x, y, win, wScreen, hScreen):
        super(T, self).__init__(x, y, win, wScreen, hScreen)
        self.width = 54
        self.height = 36
        self.t = pygame.image.load('sprite/G.png')

        self.scale()

    def scale(self):
        newWidth = (self.wScreen/10)*3
        newHeight = (self.hScreen/20)*2
        self.t = pygame.transform.scale(self.t, (round(newWidth), round(newHeight)))

    def draw(self):
        self.win.blit(self.t, (self.x, self.y))