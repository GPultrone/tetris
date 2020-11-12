import pygame
from ld import Ld
from ls import Ls
from t import T
from linea import Linea
from cubo import Cubo
from ss import Ss
from sd import Sd

clock = pygame.time.Clock()

class Tetris:
    def __init__(self, win, wScreen, hScreen):
        self.win = win
        self.wScreen = wScreen
        self.hScreen = hScreen
        self.run = True

        self.ld = Ld(53, 50, win, self.wScreen, self.hScreen)
        self.sd = Sd(353, 50, win, self.wScreen, self.hScreen)
        self.maincycle()

    def maincycle(self):
        while self.run:
            clock.tick(30)

            pygame.draw.rect(self.win, (0, 0, 0), pygame.rect.Rect(0, 0 , self.wScreen, self.hScreen))
            for i in range(1, 10):
                pygame.draw.line(self.win, (255, 255, 255), ((self.wScreen/10)*i, 0), ((self.wScreen/10)*i, self.hScreen))

            for i in range(1, 20):
                pygame.draw.line(self.win, (255, 255, 255), (0, (self.hScreen / 20) * i),(self.wScreen, (self.hScreen / 20) * i))

            self.ld.draw()
            self.sd.draw()

            for event in pygame.event.get():
                if event.type is pygame.QUIT:
                    self.run = False

            pygame.display.update()