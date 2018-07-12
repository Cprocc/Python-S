#尚未解决调试错误
class Location(object):
    def __init__(self, x, y):
        self.x, self.y = x, y
    def move(self, deltaX, deltaY):
        return Location(self.x + deltaX ,self.y + deltaY)
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def distFrom(self, other):
        ox, oy = other.x, other.y
        xDist, yDist = self.x - ox, self.y - oy
        return (xDist**2 + yDist**2)**0.5
    def __str__(self):
        return '<' + str(self.x) + ',' + str(self.y) + '>'
class Field(object):
    def __init__(self):
        self.drunks = {}
    def addDrunk(self, drunk, loc):
        if drunk in self.drunks:
            raise ValueError('Duplicate drunk')
        else:
            self.drunks[drunk] = loc
    def moveDrunk(self, drunk):
        if drunk not in (self.drunks):
            raise ValueError('Drunk not in field')
        xDist, yDist = drunk.takeStep()
        currentLocation = self.drunks[drunk]
        #使用location 的move方法获取一个新位置
        self.drunks[drunk] = currentLocation.move(xDist, yDist)
    def getLoc(self, drunk):
        if drunk not in self.drunks:
            raise ValueError('Drunk not in field')
        return self.drunks[drunk]

import random

class Drunk(object):
    def __init__(self, name = None):
        self.name = name
    def __str__(self):
        if self != None:
            return self.name
        return 'Anonymous'

class UsualDrunk(Drunk):
    def takeStep(self):
        stepChoices = [(0,1), (0,-1),(1.0), (-1,0)]
        return random.choice(stepChoices)
        return random.choice(stepChoices)

def walk(f, d, numSteps):
    start = f.getLoc(d)
    for s in range (numSteps):
        f.moveDrunk(d)
    return start.distFrom(f.getLoc(d))

def simWalks(numSteps, numTrials, dClass):
    '''dClass is the children of Drunk
        numTrials is the time of going
        numsteps is the steps of once walk'''
    Homer = dClass()
    origin = Location(0, 0)
    distances = []
    for t in range(numTrials):
        f = Field()
        f.addDrunk(Homer, origin)
        distances.append(round(walk(f, Homer, numTrials), 1))
    return distances

def drunkTest(walkLengths, numTrials, dClass):
    for numSteps in walkLengths:
        distances = simWalks(numSteps, numTrials, dClass)
        print(dClass.__name__ , 'random walk of', numSteps,'steps')
        print('Mean = ', round(sum(distances)/len(distances),4))
        print('Max = ', max(distances), 'Min = ', min(distances))
drunkTest((0, 1), 100, UsualDrunk)