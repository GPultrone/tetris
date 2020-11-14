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
        self.shift = wScreen/10
        self.indexBlockGame = 1

        self.ld = Ld(50, 50, self.win, self.wScreen, self.hScreen)
        self.ls = Ls(50, 50, self.win, self.wScreen, self.hScreen)
        self.t = T(50, 50, self.win, self.wScreen, self.hScreen)
        self.linea = Linea(50, 50, self.win, self.wScreen, self.hScreen)
        self.cubo = Cubo(50, 50, self.win, self.wScreen, self.hScreen)
        self.ss = Ss(50, 50, self.win, self.wScreen, self.hScreen)
        self.sd = Sd(50, 50, self.win, self.wScreen, self.hScreen)

        for i in range(2):
            rand = random.randint(0, 6)
            self.enumerate(rand)

        self.blockGame[self.indexBlockGame - 1].scale()
        self.blockGame[self.indexBlockGame].scaleProx()
        self.blockGame[self.indexBlockGame - 1].translation()
        self.blockGame[self.indexBlockGame].translationProx()

        self.maincycle()

    def maincycle(self):
        while self.run:
            clock.tick(30)

            self.drawGamePanel()
            self.drawBlockGame()

            for event in pygame.event.get():
                if event.type is pygame.QUIT:
                    self.run = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        if self.blockGame[self.indexBlockGame - 1].x > 50:
                            self.blockGame[self.indexBlockGame - 1].sxShift(self.shift)
                    if event.key == pygame.K_RIGHT:
                        if self.blockGame[self.indexBlockGame-1].x < self.wScreen+50-self.blockGame[self.indexBlockGame-1].width:
                            self.blockGame[self.indexBlockGame - 1].dxShift(self.shift)
                    if event.key == pygame.K_SPACE:
                        self.blockGame[self.indexBlockGame - 1].y = self.hScreen + 100 - self.blockGame[self.indexBlockGame - 1].height
                    if event.key == pygame.K_DOWN:
                        self.vel = 5

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_DOWN:
                        self.vel = 1

            pygame.display.update()

    def drawGamePanel(self):
        pygame.draw.rect(self.win, (0, 0, 0), pygame.rect.Rect(0, 0, self.wWindow, self.hWindow))
        for i in range(1, 10):
            pygame.draw.line(self.win, (255, 255, 255), (((self.wScreen / 10) * i) + 50, 100), (((self.wScreen / 10) * i) + 50, self.hScreen + 100))

        for i in range(1, 20):
            pygame.draw.line(self.win, (255, 255, 255), (50, ((self.hScreen / 20) * i) + 100), (self.wScreen + 50, ((self.hScreen / 20) * i) + 100))
        # pygame.draw.rect(self.win, (128, 128, 128), pygame.rect.Rect(50, 100, self.wScreen, self.hScreen))

    def drawBlockGame(self):
        if not (self.blockGame[self.indexBlockGame - 1].hitbox.collidepoint(self.hScreen+100)):
            rand = random.randint(0, 6)
            self.enumerate(rand)
            self.indexBlockGame += 1
            self.blockGame[self.indexBlockGame - 1].scale()
            self.blockGame[self.indexBlockGame].scaleProx()
            self.blockGame[self.indexBlockGame - 1].translation()
            self.blockGame[self.indexBlockGame].translationProx()

        self.blockGame[self.indexBlockGame - 1].moving(self.vel)

        for blockDraw in self.blockGame:
            blockDraw.draw()

    def enumerate(self, type):
        if type == 0:
            self.blockGame.append(Ld(50, 50, self.win, self.wScreen, self.hScreen))
        if type == 1:
            self.blockGame.append(Ls(50, 50, self.win, self.wScreen, self.hScreen))
        if type == 2:
            self.blockGame.append(T(50, 50, self.win, self.wScreen, self.hScreen))
        if type == 3:
            self.blockGame.append(Linea(50, 50, self.win, self.wScreen, self.hScreen))
        if type == 4:
            self.blockGame.append(Cubo(50, 50, self.win, self.wScreen, self.hScreen))
        if type == 5:
            self.blockGame.append(Ss(50, 50, self.win, self.wScreen, self.hScreen))
        if type == 6:
            self.blockGame.append(Sd(50, 50, self.win, self.wScreen, self.hScreen))