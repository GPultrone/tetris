import pygame
from sprite import Sprite

class Cubo(Sprite):
    def __init__(self, x, y, win, wScreen, hScreen):
        super(Cubo, self).__init__(x, y, win, wScreen, hScreen)
        self.width = 36
        self.height = 36
        self.cubo = pygame.image.load('sprite/V.png')

    def scale(self):
        newWidth = (self.wScreen/10)*2
        newHeight = (self.hScreen/20)*2
        self.cubo = pygame.transform.scale(self.cubo, (round(newWidth), round(newHeight)))

    def scaleProx(self):
        newWidth = (self.wScreen / 30) * 2
        newHeight = (self.hScreen / 60) * 2
        self.cubo = pygame.transform.scale(self.cubo, (round(newWidth), round(newHeight)))

    def draw(self):
        self.win.blit(self.cubo, (self.x, self.y))

    def moving(self, vel):
        self.y += vel
        self.draw()

    def translation(self):
        self.x = (self.wScreen/2) + (self.width/2)
        self.draw()

    def translationProx(self):
        self.x = 50
        self.draw()