import pygame
from sprite import Sprite

class Sd(Sprite):
    def __init__(self, x, y, win, wScreen, hScreen):
        super(Sd, self).__init__(x, y, win, wScreen, hScreen)
        self.width = 1700
        self.height = 1700
        self.color = 0
        self.lastPosition = 3
        self.newPosition = 0
        self.sd_block1 = pygame.image.load('sprite/ProvaRO.png')
        self.sd_block2 = pygame.image.load('sprite/ProvaRO.png')
        self.sd_block3 = pygame.image.load('sprite/ProvaRO.png')
        self.sd_block4 = pygame.image.load('sprite/ProvaRO.png')
        self.block1_Point = (self.x + self.width, self.y)
        self.block2_Point = (self.x, self.y + self.height)
        self.block3_Point = (self.x + self.width, self.y + self.height)
        self.block4_Point = (self.x, self.y + self.height + self.height)
        self.rectHitbox = (self.x, self.y, self.width * 2, self.height * 3)
        self.upgradeHitbox()
        self.upgradePoint()

    def scale(self):
        self.width = (self.wScreen/10)
        self.height = (self.hScreen/20)
        self.sd_block1 = pygame.transform.scale(self.sd_block1, (round(self.width), round(self.height)))
        self.sd_block2 = pygame.transform.scale(self.sd_block2, (round(self.width), round(self.height)))
        self.sd_block3 = pygame.transform.scale(self.sd_block3, (round(self.width), round(self.height)))
        self.sd_block4 = pygame.transform.scale(self.sd_block4, (round(self.width), round(self.height)))
        self.upgradeHitbox()
        self.upgradePoint()

    def scaleProx(self):
        self.width = (self.wScreen / 30)
        self.height = (self.hScreen / 60)
        self.sd_block1 = pygame.transform.scale(self.sd_block1, (round(self.width), round(self.height)))
        self.sd_block2 = pygame.transform.scale(self.sd_block2, (round(self.width), round(self.height)))
        self.sd_block3 = pygame.transform.scale(self.sd_block3, (round(self.width), round(self.height)))
        self.sd_block4 = pygame.transform.scale(self.sd_block4, (round(self.width), round(self.height)))
        self.upgradeHitbox()
        self.upgradePoint()

    def draw(self):
        self.win.blit(self.sd_block1, self.block1_Point)
        self.win.blit(self.sd_block2, self.block2_Point)
        self.win.blit(self.sd_block3, self.block3_Point)
        self.win.blit(self.sd_block4, self.block4_Point)

    def translation(self):
        self.x = (self.wScreen/2) + 50 - (self.width)
        self.upgradeHitbox()
        self.upgradePoint()

    def upgradeHitbox(self):
        self.hitbox = pygame.rect.Rect(self.rectHitbox)

    def upgradePoint(self):
        if self.newPosition == 0:
            self.block1_Point = (self.x + self.width, self.y)
            self.block2_Point = (self.x, self.y + self.height)
            self.block3_Point = (self.x + self.width, self.y + self.height)
            self.block4_Point = (self.x, self.y + self.height + self.height)
            self.rectHitbox = (self.x, self.y, self.width * 2, self.height * 3)
        if self.newPosition == 1:
            self.block1_Point = (self.x + self.width, self.y + self.height + self.height)
            self.block2_Point = (self.x, self.y + self.height)
            self.block3_Point = (self.x - self.width, self.y + self.height)
            self.block4_Point = (self.x, self.y + self.height + self.height)
            self.rectHitbox = (self.x - self.width, self.y + self.height, self.width * 3, self.height * 2)
        if self.newPosition == 2:
            self.block1_Point = (self.x, self.y)
            self.block2_Point = (self.x - self.width, self.y + self.height)
            self.block3_Point = (self.x, self.y + self.height)
            self.block4_Point = (self.x - self.width, self.y + self.height + self.height)
            self.rectHitbox = (self.x - self.width, self.y, self.width * 2, self.height * 3)
        if self.newPosition == 3:
            self.block1_Point = (self.x + self.width, self.y + self.height)
            self.block2_Point = (self.x, self.y)
            self.block3_Point = (self.x - self.width, self.y)
            self.block4_Point = (self.x, self.y + self.height)
            self.rectHitbox = (self.x - self.width, self.y, self.width * 3, self.height * 2)