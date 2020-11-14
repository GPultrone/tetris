import pygame
from sprite import Sprite

class Ls(Sprite):
    def __init__(self, x, y, win, wScreen, hScreen):
        super(Ls, self).__init__(x, y, win, wScreen, hScreen)
        self.ls = pygame.image.load('sprite/ProvaVE.png')
        self.width = 17
        self.height = 17
        self.hitbox = pygame.rect.Rect(self.x, self.y, self.width*3, self.height*2)

    def scale(self):
        self.width = (self.wScreen/10)
        self.height = (self.hScreen/20)
        self.ls = pygame.transform.scale(self.ls, (round(self.width), round(self.height)))
        self.upgradeHitbox()

    def scaleProx(self):
        self.width = (self.wScreen / 30)
        self.height = (self.hScreen / 60)
        self.ls = pygame.transform.scale(self.ls, (round(self.width), round(self.height)))
        self.upgradeHitbox()

    def draw(self):
        self.win.blit(self.ls, (self.x, self.y))
        self.win.blit(self.ls, (self.x+self.width, self.y))
        self.win.blit(self.ls, (self.x+self.width+self.width, self.y))
        self.win.blit(self.ls, (self.x, self.y+self.height))

    def translation(self):
        self.x = (self.wScreen/2) - 50 + self.width - (self.width/2)
        self.upgradeHitbox()