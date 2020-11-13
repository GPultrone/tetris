import pygame
from sprite import Sprite

class Linea(Sprite):
    def __init__(self, x, y, win, wScreen, hScreen):
        super(Linea, self).__init__(x, y, win, wScreen, hScreen)
        self.width = 18
        self.height = 72
        self.linea = pygame.image.load('sprite/A.png')

    def scale(self):
        newWidth = (self.wScreen/10)
        newHeight = (self.hScreen/20)*4
        self.linea = pygame.transform.scale(self.linea, (round(newWidth), round(newHeight)))

    def scaleProx(self):
        newWidth = (self.wScreen / 30)
        newHeight = (self.hScreen / 60) * 4
        self.linea = pygame.transform.scale(self.linea, (round(newWidth), round(newHeight)))

    def draw(self):
        self.win.blit(self.linea, (self.x, self.y))

    def moving(self, vel):
        self.y += vel
        self.draw()

    def translation(self):
        self.x = (self.wScreen/2) + (self.width/2)
        self.draw()

    def translationProx(self):
        self.x = 50
        self.draw()