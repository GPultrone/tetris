import pygame
from sprite import Sprite

class Ss(Sprite):
    def __init__(self, x, y, win, wScreen, hScreen):
        super(Ss, self).__init__(x, y, win, wScreen, hScreen)
        self.width = 35
        self.height = 54
        self.ss = pygame.image.load('sprite/VA.png')

    def scale(self):
        newWidth = (self.wScreen/10)*2
        newHeight = (self.hScreen/20)*3
        self.ss = pygame.transform.scale(self.ss, (round(newWidth), round(newHeight)))

    def scaleProx(self):
        newWidth = (self.wScreen / 30) * 2
        newHeight = (self.hScreen / 60) * 3
        self.ss = pygame.transform.scale(self.ss, (round(newWidth), round(newHeight)))

    def draw(self):
        self.win.blit(self.ss, (self.x, self.y))

    def moving(self, vel):
        self.y += vel
        self.draw()

    def translation(self):
        self.x = (self.wScreen/2) + (self.width/2)
        self.draw()

    def translationProx(self):
        self.x = 50
        self.draw()