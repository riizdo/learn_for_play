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
        self.__font = 'purisa'
        self.points = 0
        self.select = 0

        self.__elements = []
        self.__exercisesList = []

        #self.__font
        self.__fontSize = 50

        self.__label = menu.Label('hola', self.__fontSize, self.__font)
        self.__label.center(self.__margin)


    def addExercise(self, exercise):
        self.__exercisesList.append(exercise)


    def addExercisesList(self, exercises):
        for exercise in exercises:
            exercise['finish'] = False
            exercise['userResult'] = []
            result = str(exercise['result'])
            for r in result:
                exercise['userResult'].append(0)
            self.__exercisesList.append(exercise)


    def finishExercise(self, exercise):
        result = ''
        counter = 0
        for element in reversed(exercise['userResult']):
            element = str(element)
            result += element
        result = int(result)
        if result == exercise['result']:
            self.points += 1
        for element in self.__exercisesList:
            print(element, exercise)
            if element['id'] == exercise['id']:
                self.__exercisesList[counter]['finish'] = True
            counter += 1


    def calculateColumn(self, element, type):
        result = 0
        latest = type[len(type) -1]
        if type == 'element' or type == 'line':
            element = str(element)
            for i in range(0, len(element)):
                result += 10
        elif latest.isdigit() and type == 'result' + latest:
            latest = int(latest)
            result = 20 * latest
        return result


    def updateExercises(self):
        for exercise in self.__exercisesList:
            if exercise['finish'] == False:
                return exercise


    def drawExercise(self, exercise):
        print(exercise)
        labels = []
        column = 100
        counter = 0
        lineText = ''
        
        for element in exercise['element']:
            element = str(element)
            print('draw: ' + element)
            columnElement = column - self.calculateColumn(element, 'element')
            label = menu.Label(element, self.__fontSize, self.__font)
            label.pos(columnElement, counter)
            label.draw(self.__screen, element)
            labels.append(label)
            counter += 50
        
        for i in range(0, len(str(exercise['result']))):
            lineText += '_'
        line = menu.Label(lineText, self.__fontSize, self.__font)
        columnLine = column - self.calculateColumn(lineText, 'line')
        line.pos(columnLine, counter - 45)
        line.draw(self.__screen, lineText)

        operation = menu.Label(exercise['operation'], self.__fontSize, self.__font)
        operation.pos(70, counter - 55)
        operation.draw(self.__screen, exercise['operation'])

        columnResult = 0
        counterResult = 0
        for element in exercise['userResult']:
            columnResult = column - self.calculateColumn(element, 'result' + str(counterResult))
            element = str(element)
            labelResult = menu.Label(element, self.__fontSize, self.__font)
            labelResult.pos(columnResult, counter)
            labelResult.draw(self.__screen, element)
            counterResult += 1


    def start(self):
        state = True
        while state:
            exercise = self.updateExercises()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    state = False
                if event.type == pygame.KEYUP:
                    if event.key == K_ESCAPE:
                        state = False
                    if event.key == K_LEFT:
                        if self.select == len(exercise['userResult']) - 1:
                            self.select = 0
                        else:
                            self.select += 1
                    if event.key == K_RIGHT:
                        if self.select == 0:
                            self.select = len(exercise['userResult'] - 1)
                        else:
                            self.select -= 1
                    if event.key == K_UP:
                        if exercise['userResult'][self.select] == 9:
                            exercise['userResult'][self.select] = 0
                        else:
                            exercise['userResult'][self.select] += 1
                    if event.key == K_DOWN:
                        if exercise['userResult'][self.select] == 0:
                            exercise['userResult'][self.select] = 9
                        else:
                            exercise['userResult'][self.select] -= 1
                    if event.key == K_RETURN:
                        self.finishExercise(exercise)
 
            self.__screen.fill(self.__background)

            self.drawExercise(exercise)
            
            self.__label.draw(self.__screen, 'hola')
            pygame.display.flip()

        return self.points

            
            
            
if __name__ == '__main__':
    pass