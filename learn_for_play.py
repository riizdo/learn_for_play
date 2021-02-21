# archive:      learn_for_play.py
# author:       riizdo
# date:         21-02-2021
# description:  main file of the program


import os
import exercise, screen

class LearnForPlay():
    def __init__(self):
        self.user = os.getlogin()
        self.configuration = self.getConfig()
        self.time = 0
        self.level = 0
        self.points = 0
        self.exercises = []

        self.setSession()

        self.setExercises(self.level)

        self.screen = screen.Screen()

        #exercise = self.adds.getExercise()

        self.screen.addExercisesList(self.exercises)

        self.start()
    

    def getUser(self):
        return os.getlogin()


    def getConfig(self):
        configuration = {}
        file = ''
        try:
            with open('config.txt') as f:
                file = f.read()
        except:
            pass
        if file == [] or file == '' or file == None:
            self.createConfig()
            self.getConfig()
        else:
            lines = file.split('\n')
            for line in lines:
                words = line.split(' ')
                counter = 0
                title = ''
                for word in words:
                    if counter == 0:
                        title = word
                        configuration[title] = []
                    else:
                        configuration[title].append(word)
                    counter += 1

        return configuration

    
    def createConfig(self):
        with open('config.txt', 'w') as f:
            f.write('users\n')
            f.write('timeForPoint\n')


    def setSession(self):
        file = ''
        try:
            with open(self.user + 'Session.txt') as f:
                file = f.read()
        except:
            pass
        if file == [] or file == '' or file == None:
            self.time = 0
            self.level = 0
            self.points = 0
        else:
            lines = file.split('\n')
            for line in lines:
                words = line.split(' ')
                if words[0] == 'time':
                    if len(words) > 1:
                        self.time = words[1]
                elif words[0] == 'level':
                    if len(words) > 1:
                        self.level = words[1]
                elif words[0] == 'points':
                    if len(words) > 1:
                        self.points = words[1]


    def saveSession(self):
        with open(self.user + 'Session.txt', 'w') as f:
            f.write('time ' + self.time + '\n')
            f.write('level' + self.level + '\n')
            f.write('points' + self.points + '\n')


    def setExercises(self, level = None):
        nExercises = 0
        if level == None:
            self.level = 0
            level = 0
        if level < 10:
            nExercises = 5
        elif level < 20:
            nExercises = 7
        elif level < 30:
            nExercises = 10
        else:
            nExercises = 10
        for i in range(0, nExercises):
            e = exercise.Adds(level, i)
            self.exercises.append(e.getExercise())


    def start(self):
        self.points += self.screen.start()
        print('points: ', self.points)



if __name__ == '__main__':
    app = LearnForPlay()