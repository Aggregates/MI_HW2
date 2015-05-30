import random

class MonteCarlo(object):

    def __init__(self, target, stepSize):
        self.state = 0
        self.targetValue = target
        self.stepSize = stepSize
        self.stateValue = 0


    def nextMove(self):
        '''
        Decide which direction to move in.
        Chosen direction will be between 1 and 4 (inclusive)
        '''

        direction = random.randint(1,4)
        return direction

    def temporalDifference(self):
        stateValue = self.predictValue(state) + stepSize * (self.targetValue - self.predictValue(state))


    def predictValue(self, state, time):
        return 1

if __name__ == "__main__":
    print nextMove()
