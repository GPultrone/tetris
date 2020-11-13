import pygame
from sprite import Sprite

class Ls(Sprite):
    def __init__(self, x, y, win, wScreen, hScreen):
        super(Ls, self).__init__(x, y, win, wScreen, hScreen)
        self.width = 54
        self.height = 36
        self.ls = pygame.image.load('sprite/VE.png')

    def scale(self):
        newWidth = (self.wScreen/10)*3
        newHeight = (self.hScreen/20)*2
        self.ls = pygame.transform.scale(self.ls, (round(newWidth), round(newHeight)))

    def scaleProx(self):
        newWidth = (self.wScreen / 30) * 3
        newHeight = (self.hScreen / 60) * 2
        self.ls = pygame.transform.scale(self.ls, (round(newWidth), round(newHeight)))

    def draw(self):
        self.win.blit(self.ls, (self.x, self.y))

    def moving(self, vel):
        self.y += vel
        self.draw()

    def translation(self):
        self.x = (self.wScreen/2) + (self.width/2)
        self.draw()

    def translationProx(self):
        self.x = 50
        self.draw()