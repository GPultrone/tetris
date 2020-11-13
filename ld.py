import pygame
from sprite import Sprite

class Ld(Sprite):
    def __init__(self, x, y, win, wScreen, hScreen):
        super(Ld, self).__init__(x, y, win, wScreen, hScreen)
        self.width = 54
        self.height = 36
        self.ld = pygame.image.load('sprite/R.png')
        self.hitbox = pygame.rect.Rect(self.x, self.y, self.width, self.height)

    def scale(self):
        self.width = (self.wScreen/10)*3
        self.height = (self.hScreen/20)*2
        self.ld = pygame.transform.scale(self.ld, (round(self.width), round(self.height)))
        self.upgradeHitbox()

    def scaleProx(self):
        self.width = (self.wScreen / 30) * 3
        self.height = (self.hScreen / 60) * 2
        self.ld = pygame.transform.scale(self.ld, (round(self.width), round(self.height)))
        self.upgradeHitbox()

    def draw(self):
        self.win.blit(self.ld, (self.x, self.y))

    def translation(self):
        self.x = (self.wScreen/2) - 50 + self.width - (self.width/2)
        self.upgradeHitbox()