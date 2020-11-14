import pygame
from sprite import Sprite

class Ss(Sprite):
    def __init__(self, x, y, win, wScreen, hScreen):
        super(Ss, self).__init__(x, y, win, wScreen, hScreen)
        self.width = 17
        self.height = 17
        self.ss = pygame.image.load('sprite/ProvaVA.png')
        self.hitbox = pygame.rect.Rect(self.x, self.y, self.width*2, self.height*3)

    def scale(self):
        self.width = (self.wScreen/10)
        self.height = (self.hScreen/20)
        self.ss = pygame.transform.scale(self.ss, (round(self.width), round(self.height)))
        self.upgradeHitbox()

    def scaleProx(self):
        self.width = (self.wScreen / 30)
        self.height = (self.hScreen / 60)
        self.ss = pygame.transform.scale(self.ss, (round(self.width), round(self.height)))
        self.upgradeHitbox()

    def draw(self):
        self.win.blit(self.ss, (self.x, self.y))
        self.win.blit(self.ss, (self.x, self.y + self.height))
        self.win.blit(self.ss, (self.x + self.width, self.y + self.height))
        self.win.blit(self.ss, (self.x + self.width, self.y + self.height + self.height))

    def translation(self):
        self.x = (self.wScreen/2) + 50 - (self.width)
        self.upgradeHitbox()