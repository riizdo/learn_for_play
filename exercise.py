# archive:      exercise.py
# author:       riizdo
# date:         16-02-2021
# description:  exercises file 

import pygame
from pygame.locals import *
import random


class Exercise():
    def __init__(self, level, id):
        self.level = level
        self.elements = {}
        self.elements['id'] = id
        self.elements['element'] = []
        self.elements['operation'] = []


    def getExercise(self):
        return self.elements


    def getElements(self):
        elements = []
        for element in self.elements:
            if element == 'element':
                elements.append(self.elements[element])
        return elements


    def getOperation(self):
        operations = []
        for element in self.elements:
            if element == 'operation':
                operations.append(self.elements[element])
        return operations


    def getResult(self):
        for element in self.elements:
            if element == 'result':
                return self.elements[element]
            
    



class Adds(Exercise):
    def __init__(self, level, id):
        Exercise.__init__(self, level, id)
        self.elements['operation'] = '+'

        nElements = self.getNElements()

        self.defineElements(nElements)
        self.elements['result'] = self.defineResult()


    def getNElements(self):
        if self.level < 75:
            return 2
        elif self.level < 90:
            return 3
        else:
            return 4


    def defineElements(self, nElements):
        max = 0

        if self.level < 10:
            max = 10
        elif self.level < 20:
            max = 50
        elif self.level < 30:
            max = 100
        else:
            max = 1000

        for i in range(0, nElements):
            n = random.randrange(0, max)
            self.elements['element'].append(n)


    def defineResult(self):
        result = 0
        for element in self.elements:
            if element == 'element':
                for num in self.elements[element]:
                    result += num
        return result

