import pygame
from sprite import Sprite

class Sd(Sprite):
    def __init__(self, x, y, win, wScreen, hScreen):
        super(Sd, self).__init__(x, y, win, wScreen, hScreen)
        self.width = 17
        self.height = 17
        self.sd = pygame.image.load('sprite/ProvaRO.png')
        self.hitbox = pygame.rect.Rect(self.x, self.y, self.width*2, self.height*3)

    def scale(self):
        self.width = (self.wScreen/10)
        self.height = (self.hScreen/20)
        self.sd = pygame.transform.scale(self.sd, (round(self.width), round(self.height)))
        self.upgradeHitbox()

    def scaleProx(self):
        self.width = (self.wScreen / 30)
        self.height = (self.hScreen / 60)
        self.sd = pygame.transform.scale(self.sd, (round(self.width), round(self.height)))
        self.upgradeHitbox()

    def draw(self):
        self.win.blit(self.sd, (self.x + self.width, self.y))
        self.win.blit(self.sd, (self.x, self.y + self.height))
        self.win.blit(self.sd, (self.x + self.width, self.y + self.height))
        self.win.blit(self.sd, (self.x, self.y + self.height + self.height))

    def translation(self):
        self.x = (self.wScreen/2) + 50 - (self.width)
        self.upgradeHitbox()