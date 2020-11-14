import pygame
from sprite import Sprite

class Ss(Sprite):
    def __init__(self, x, y, win, wScreen, hScreen):
        super(Ss, self).__init__(x, y, win, wScreen, hScreen)
        self.width = 1700
        self.height = 1700
        self.color = 1
        self.ss_block1 = pygame.image.load('sprite/ProvaVA.png')
        self.ss_block2 = pygame.image.load('sprite/ProvaVA.png')
        self.ss_block3 = pygame.image.load('sprite/ProvaVA.png')
        self.ss_block4 = pygame.image.load('sprite/ProvaVA.png')
        self.block1_Point = (self.x, self.y)
        self.block2_Point = (self.x, self.y + self.height)
        self.block3_Point = (self.x + self.width, self.y + self.height)
        self.block4_Point = (self.x + self.width, self.y + self.height + self.height)
        self.upgradeHitbox()
        self.upgradePoint()

    def scale(self):
        self.width = (self.wScreen/10)
        self.height = (self.hScreen/20)
        self.ss_block1 = pygame.transform.scale(self.ss_block1, (round(self.width), round(self.height)))
        self.ss_block2 = pygame.transform.scale(self.ss_block2, (round(self.width), round(self.height)))
        self.ss_block3 = pygame.transform.scale(self.ss_block3, (round(self.width), round(self.height)))
        self.ss_block4 = pygame.transform.scale(self.ss_block4, (round(self.width), round(self.height)))
        self.upgradeHitbox()
        self.upgradePoint()

    def scaleProx(self):
        self.width = (self.wScreen / 30)
        self.height = (self.hScreen / 60)
        self.ss_block1 = pygame.transform.scale(self.ss_block1, (round(self.width), round(self.height)))
        self.ss_block2 = pygame.transform.scale(self.ss_block2, (round(self.width), round(self.height)))
        self.ss_block3 = pygame.transform.scale(self.ss_block3, (round(self.width), round(self.height)))
        self.ss_block4 = pygame.transform.scale(self.ss_block4, (round(self.width), round(self.height)))
        self.upgradeHitbox()
        self.upgradePoint()

    def draw(self):
        self.win.blit(self.ss_block1, self.block1_Point)
        self.win.blit(self.ss_block2, self.block2_Point)
        self.win.blit(self.ss_block3, self.block3_Point)
        self.win.blit(self.ss_block4, self.block4_Point)

    def translation(self):
        self.x = (self.wScreen/2) + 50 - (self.width)
        self.upgradeHitbox()
        self.upgradePoint()

    def upgradeHitbox(self):
        self.hitbox = pygame.rect.Rect(self.x, self.y, self.width*2, self.height*3)

    def upgradePoint(self):
        self.block1_Point = (self.x, self.y)
        self.block2_Point = (self.x, self.y + self.height)
        self.block3_Point = (self.x + self.width, self.y + self.height)
        self.block4_Point = (self.x + self.width, self.y + self.height + self.height)