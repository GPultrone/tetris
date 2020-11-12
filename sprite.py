import pygame

ls = pygame.image.load('sprite/VE.png')
t = pygame.image.load('sprite/G.png')
linea = pygame.image.load('sprite/A.png')
cubo = pygame.image.load('sprite/V.png')
ss = pygame.image.load('sprite/VA.png')
sd = pygame.image.load('sprite/RO.png')

class Sprite:
    def __init__(self, x, y, win, wScreen, hScreen):
        self.x = x
        self.y = y
        self.win = win
        self.wScreen = wScreen
        self.hScreen = hScreen
