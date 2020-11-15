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
        self.upgradePoint()

    def translationProx(self):
        self.x = 50
        self.upgradeHitbox()
        self.upgradePoint()

    def sxShift(self, shift):
        self.x -= shift
        self.upgradeHitbox()
        self.upgradePoint()

    def dxShift(self, shift):
        self.x += shift
        self.upgradeHitbox()
        self.upgradePoint()

    def clockwiseRotation(self):
        if self.newPosition == 0:
            self.lastPosition = 0
            self.newPosition = 1
            self.upgradePoint()
        elif self.newPosition == 1:
            self.lastPosition = 1
            self.newPosition = 2
            self.upgradePoint()
        elif self.newPosition == 2:
            self.lastPosition = 2
            self.newPosition = 3
            self.upgradePoint()
        elif self.newPosition == 3:
            self.lastPosition = 3
            self.newPosition = 0
            self.upgradePoint()

    def reverseclockwiseRotation(self):
        if self.newPosition == 0:
            self.lastPosition = 0
            self.newPosition = 3
            self.upgradePoint()
        elif self.newPosition == 1:
            self.lastPosition = 1
            self.newPosition = 0
            self.upgradePoint()
        elif self.newPosition == 2:
            self.lastPosition = 2
            self.newPosition = 1
            self.upgradePoint()
        elif self.newPosition == 3:
            self.lastPosition = 3
            self.newPosition = 2
            self.upgradePoint()