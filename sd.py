import pygame
from sprite import Sprite

class Sd(Sprite):
    def __init__(self, x, y, win, wScreen, hScreen):
        super(Sd, self).__init__(x, y, win, wScreen, hScreen)
        self.width = 35
        self.height = 54
        self.sd = pygame.image.load('sprite/RO.png')
        self.hitbox = pygame.rect.Rect(self.x, self.y, self.width, self.height)

    def scale(self):
        self.width = (self.wScreen/10)*2
        self.height = (self.hScreen/20)*3
        self.sd = pygame.transform.scale(self.sd, (round(self.width), round(self.height)))
        self.upgradeHitbox()

    def scaleProx(self):
        self.width = (self.wScreen / 30) * 2
        self.height = (self.hScreen / 60) * 3
        self.sd = pygame.transform.scale(self.sd, (round(self.width), round(self.height)))
        self.upgradeHitbox()

    def draw(self):
        self.win.blit(self.sd, (self.x, self.y))

    def translation(self):
        self.x = (self.wScreen/2) + 50 - (self.width/2)
        self.upgradeHitbox()