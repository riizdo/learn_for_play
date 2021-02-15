import pygame, os
from pygame.locals import *


YELLOW = (150, 150, 0)
RED = (0, 0, 150)

class Screen():
    def __init__(self):
        pygame.init()
        self.__background = YELLOW
        self.__screenSize = (1400, 800)
        self.__screen = pygame.display.set_mode(self.__screenSize)
        pygame.FULLSCREEN
        pygame.display.set_caption('learn for play')
        self.__screen.fill(self.__background)
        
        
    def start(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    
            self.__screen.fill(self.__background)
            pygame.display.flip()
            
            
            
if __name__ == '__main__':
    app = Screen()
    app.start()