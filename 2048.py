import os
import random
import pygame
import time
from Games.Game2048.logic import setmode, randomstate, gameOver, fillMatrix

pygame.init()

rootPath = os.path.abspath(os.path.dirname(__file__))
imagePath = os.path.join(rootPath, 'img')

def loadIMAGES(number):
    numPath = os.path.join(imagePath, "{}.png".format(number))
    numImage = pygame.image.load(numPath)
    return numImage

class GAME:
    def __init__(self):
        self.width = 410
        self.height = 450
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.run = True
        self.state = randomstate()
        self.laststate = self.state
        self.moves = 0

        # set background
        self.backgroundPath = os.path.join(imagePath, "game.png")
        self.backgroundImage = pygame.image.load(self.backgroundPath)
        self.backgroundImage = pygame.transform.scale(self.backgroundImage, (self.width, self.height))

    def gameLoop(self):
        while self.run:
            self.laststate = self.state
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                if event.type == pygame.KEYDOWN:
                    if gameOver(array=self.state):
                        print('game is over')
                        time.sleep(5)
                        self.run = False

                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        self.state = setmode(array=self.state, mode='up')

                    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        self.state = setmode(array=self.state, mode='down')

                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        self.state = setmode(array=self.state, mode='left')

                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        self.state = setmode(array=self.state, mode='right')

                    if self.laststate != self.state:
                        self.state = fillMatrix(array=self.state)


            self.screen.blit(self.backgroundImage, (0, 0))
            self.screen.blit(loadIMAGES(self.state[0][0]), (30, 80))
            self.screen.blit(loadIMAGES(self.state[0][1]), (30 + 90, 80))
            self.screen.blit(loadIMAGES(self.state[0][2]), (30 + 180, 80))
            self.screen.blit(loadIMAGES(self.state[0][3]), (30 + 270, 80))

            self.screen.blit(loadIMAGES(self.state[1][0]), (30, 170))
            self.screen.blit(loadIMAGES(self.state[1][1]), (30 + 90, 170))
            self.screen.blit(loadIMAGES(self.state[1][2]), (30 + 180, 170))
            self.screen.blit(loadIMAGES(self.state[1][3]), (30 + 270, 170))

            self.screen.blit(loadIMAGES(self.state[2][0]), (30, 260))
            self.screen.blit(loadIMAGES(self.state[2][1]), (30 + 90, 260))
            self.screen.blit(loadIMAGES(self.state[2][2]), (30 + 180, 260))
            self.screen.blit(loadIMAGES(self.state[2][3]), (30 + 270, 260))

            self.screen.blit(loadIMAGES(self.state[3][0]), (30, 350))
            self.screen.blit(loadIMAGES(self.state[3][1]), (30 + 90, 350))
            self.screen.blit(loadIMAGES(self.state[3][2]), (30 + 180, 350))
            self.screen.blit(loadIMAGES(self.state[3][3]), (30 + 270, 350))

            pygame.display.update()


GAME().gameLoop()
