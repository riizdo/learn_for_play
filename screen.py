# archive:      screen.py
# author:       riizdo
# date:         15-02-2021
# description:  window file

import pygame, os
from pygame.locals import *


YELLOW = (150, 150, 0)
RED = (0, 0, 150)
WHITE = (255, 255, 255)

class Screen():
    def __init__(self):
        pygame.init()
        self.__background = YELLOW
        self.__screenSize = (1400, 800)
        self.__screen = pygame.display.set_mode(self.__screenSize)
        pygame.FULLSCREEN
        pygame.display.set_caption('learn for play')
        self.__screen.fill(self.__background)

        #self.__font
        self.__fontSize = 16
        self.exist = False


    def testFont(self):
        self.__textPos = 0
        for element in pygame.font.get_fonts():
            try:   
                self.__font = element
                text = 'hola ' + element
                tFont = pygame.font.sysFont(self.__font, self.__fontSize)

            
                self.__surfaceText = tFont.render(text, True, WHITE)
                self.exist = True
            except:
                self.exist = False
                pass

            self.__textPos += 15
        
        
    def start(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    break
                    
            self.__screen.fill(self.__background)
            if self.exist:
                self.__screen.blit(self.__surfaceText, (0, self.__textPos))
            pygame.display.flip()


    def exit(self):
        pygame.quit()
            
            
            
if __name__ == '__main__':
    app = Screen()
    app.start()