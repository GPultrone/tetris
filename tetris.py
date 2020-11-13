import pygame
import random
from sprite import Sprite
from ld import Ld
from ls import Ls
from t import T
from linea import Linea
from cubo import Cubo
from ss import Ss
from sd import Sd

clock = pygame.time.Clock()
array = []

class Tetris:
    def __init__(self, win, wScreen, hScreen, wWindow, hWindow):
        self.win = win
        self.wScreen = wScreen
        self.hScreen = hScreen
        self.wWindow = wWindow
        self.hWindow = hWindow
        self.run = True
        self.blockGame = []
        self.vel = 1
        self.indexBlockGame = 1

        self.ld = Ld(50, 50, self.win, self.wScreen, self.hScreen)
        self.ls = Ls(50, 50, self.win, self.wScreen, self.hScreen)
        self.t = T(50, 50, self.win, self.wScreen, self.hScreen)
        self.linea = Linea(50, 50, self.win, self.wScreen, self.hScreen)
        self.cubo = Cubo(50, 50, self.win, self.wScreen, self.hScreen)
        self.ss = Ss(50, 50, self.win, self.wScreen, self.hScreen)
        self.sd = Sd(50, 50, self.win, self.wScreen, self.hScreen)

        array.append(self.ld)
        array.append(self.ls)
        array.append(self.t)
        array.append(self.linea)
        array.append(self.cubo)
        array.append(self.ss)
        array.append(self.sd)

        for i in range(2):
            rand = random.randint(0, 6)
            self.block = array[rand]
            self.blockGame.append(self.block)

        self.maincycle()

    def maincycle(self):
        while self.run:
            clock.tick(30)

            self.drawGamePanel()

            if self.blockGame[self.indexBlockGame-1].y == 400:
                rand = random.randint(0, 6)
                self.block = array[rand]
                self.blockGame.append(self.block)
                self.indexBlockGame += 1

            self.blockGame[self.indexBlockGame-1].scale()
            self.blockGame[self.indexBlockGame-1].translation()
            self.blockGame[self.indexBlockGame-1].moving(self.vel)
            self.blockGame[self.indexBlockGame].scaleProx()
            self.blockGame[self.indexBlockGame].translationProx()
            for i in range(0, len(self.blockGame)):
                self.blockGame[i].draw()

            for event in pygame.event.get():
                if event.type is pygame.QUIT:
                    self.run = False

            pygame.display.update()

    def drawGamePanel(self):
        pygame.draw.rect(self.win, (0, 0, 0), pygame.rect.Rect(0, 0, self.wWindow, self.hWindow))
        for i in range(1, 10):
            pygame.draw.line(self.win, (255, 255, 255), (((self.wScreen / 10) * i) + 50, 100), (((self.wScreen / 10) * i) + 50, self.hScreen + 100))

        for i in range(1, 20):
            pygame.draw.line(self.win, (255, 255, 255), (50, ((self.hScreen / 20) * i) + 100), (self.wScreen + 50, ((self.hScreen / 20) * i) + 100))
        # pygame.draw.rect(self.win, (128, 128, 128), pygame.rect.Rect(50, 100, self.wScreen, self.hScreen))