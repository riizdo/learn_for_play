# archive:      learn_for_play.py
# author:       riizdo
# date:         21-02-2021
# description:  main file of the program


import os

class LearnForPlay():
    def __init__(self):
        self.user = os.getlogin()
        self.configuration = self.getConfig()
        self.time = 0


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
        with open('config.txt') as f:
            f.write('users\n')
            f.write('timeForPoint\n')


    def saveSession(self):
        with open(self.user + 'Session.txt') as f:
            f.write('time ' + self.time)



if __name__ == '__main__':
    app = LearnForPlay()