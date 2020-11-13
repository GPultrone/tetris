import pygame
from sprite import Sprite

class Linea(Sprite):
    def __init__(self, x, y, win, wScreen, hScreen):
        super(Linea, self).__init__(x, y, win, wScreen, hScreen)
        self.width = 18
        self.height = 72
        self.linea = pygame.image.load('sprite/A.png')
        self.hitbox = pygame.rect.Rect(self.x, self.y, self.width, self.height)

    def scale(self):
        self.width = (self.wScreen/10)
        self.height = (self.hScreen/20)*4
        self.linea = pygame.transform.scale(self.linea, (round(self.width), round(self.height)))
        self.upgradeHitbox()

    def scaleProx(self):
        self.width = (self.wScreen / 30)
        self.height = (self.hScreen / 60) * 4
        self.linea = pygame.transform.scale(self.linea, (round(self.width), round(self.height)))
        self.upgradeHitbox()

    def draw(self):
        self.win.blit(self.linea, (self.x, self.y))

    def translation(self):
        self.x = (self.wScreen/2) + 50 - self.width
        self.upgradeHitbox()