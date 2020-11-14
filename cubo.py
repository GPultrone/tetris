import pygame
from sprite import Sprite

class Cubo(Sprite):
    def __init__(self, x, y, win, wScreen, hScreen):
        super(Cubo, self).__init__(x, y, win, wScreen, hScreen)
        self.width = 17
        self.height = 17
        self.cubo = pygame.image.load('sprite/ProvaV.png')
        self.hitbox = pygame.rect.Rect(self.x, self.y, self.width*2, self.height*2)

    def scale(self):
        self.width = (self.wScreen/10)
        self.height = (self.hScreen/20)
        self.cubo = pygame.transform.scale(self.cubo, (round(self.width), round(self.height)))
        self.upgradeHitbox()

    def scaleProx(self):
        self.width = (self.wScreen / 30)
        self.height = (self.hScreen / 60)
        self.cubo = pygame.transform.scale(self.cubo, (round(self.width), round(self.height)))
        self.upgradeHitbox()

    def draw(self):
        self.win.blit(self.cubo, (self.x, self.y))
        self.win.blit(self.cubo, (self.x + self.width, self.y))
        self.win.blit(self.cubo, (self.x, self.y + self.height))
        self.win.blit(self.cubo, (self.x + self.width, self.y + self.height))

    def translation(self):
        self.x = (self.wScreen/2) + 50 - (self.width)
        self.upgradeHitbox()