# archive:      screen.py
# author:       riizdo
# date:         15-02-2021
# description:  window file

import pygame, os
from pygame.locals import *
import menu


YELLOW = (150, 150, 0)
RED = (0, 0, 150)
WHITE = (255, 255, 255)

class Screen():
    def __init__(self):
        pygame.init()
        self.__background = YELLOW
        self.__screenSize = (1400, 800)
        self.__screen = pygame.display.set_mode(flags = pygame.FULLSCREEN)
        pygame.display.set_caption('learn for play')
        self.__screen.fill(self.__background)
        self.__margin = self.__screen.get_rect()

        self.__elements = []
        self.__dataExercise = []

        #self.__font
        self.__fontSize = 50

        self.__label = menu.Label('hola', self.__fontSize, 'purisa')
        self.__label.center(self.__margin)


    def addExercise(self, exercise):
        self.__dataExercise.clear()
        for element in exercise:
            self.__dataExercise.append(element)


    def start(self):
        state = True
        while state:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    state = False
                if event.type == pygame.KEYUP:
                    if event.key == K_ESCAPE:
                        state = False
                    
            self.__screen.fill(self.__background)
            
            self.__label.draw(self.__screen, 'hola')
            pygame.display.flip()

            
            
            
if __name__ == '__main__':
    app = Screen()
    app.start()