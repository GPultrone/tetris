import pygame
from sprite import Sprite

class Ls(Sprite):
    def __init__(self, x, y, win, wScreen, hScreen):
        super(Ls, self).__init__(x, y, win, wScreen, hScreen)
        self.width = 54
        self.height = 36
        self.ls = pygame.image.load('sprite/VE.png')
        self.hitbox = pygame.rect.Rect(self.x, self.y, self.width, self.height)

    def scale(self):
        self.width = (self.wScreen/10)*3
        self.height = (self.hScreen/20)*2
        self.ls = pygame.transform.scale(self.ls, (round(self.width), round(self.height)))
        self.upgradeHitbox()

    def scaleProx(self):
        self.width = (self.wScreen / 30) * 3
        self.height = (self.hScreen / 60) * 2
        self.ls = pygame.transform.scale(self.ls, (round(self.width), round(self.height)))
        self.upgradeHitbox()

    def draw(self):
        self.win.blit(self.ls, (self.x, self.y))

    def translation(self):
        self.x = (self.wScreen/2) - 50 + self.width - (self.width/2)
        self.upgradeHitbox()