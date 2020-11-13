import pygame
from sprite import Sprite

class Cubo(Sprite):
    def __init__(self, x, y, win, wScreen, hScreen):
        super(Cubo, self).__init__(x, y, win, wScreen, hScreen)
        self.width = 36
        self.height = 36
        self.cubo = pygame.image.load('sprite/V.png')
        self.hitbox = pygame.rect.Rect(self.x, self.y, self.width, self.height)

    def scale(self):
        self.width = (self.wScreen/10)*2
        self.height = (self.hScreen/20)*2
        self.cubo = pygame.transform.scale(self.cubo, (round(self.width), round(self.height)))
        self.upgradeHitbox()

    def scaleProx(self):
        self.width = (self.wScreen / 30) * 2
        self.height = (self.hScreen / 60) * 2
        self.cubo = pygame.transform.scale(self.cubo, (round(self.width), round(self.height)))
        self.upgradeHitbox()

    def draw(self):
        self.win.blit(self.cubo, (self.x, self.y))

    def translation(self):
        self.x = (self.wScreen/2) + 50 - (self.width/2)
        self.upgradeHitbox()