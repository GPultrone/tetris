import pygame

class Sprite:
    def __init__(self, x, y, win, wScreen, hScreen):
        self.x = x
        self.y = y
        self.win = win
        self.wScreen = wScreen
        self.hScreen = hScreen

    def moving(self, vel):
        self.y += vel
        self.upgradeHitbox()

    def translationProx(self):
        self.x = 50
        self.upgradeHitbox()

    def sxShift(self, shift):
        self.x -= shift
        self.upgradeHitbox()

    def dxShift(self, shift):
        self.x += shift
        self.upgradeHitbox()

    def upgradeHitbox(self):
        self.hitbox = pygame.rect.Rect(self.x, self.y, self.width, self.height)