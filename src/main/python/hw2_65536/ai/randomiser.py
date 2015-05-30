import random

class Randomiser(object):

    def nextMove(self, lowerBound, upperBound):
        '''
        Gets a random move between lowerBound and upperBound (inclusive)
        '''

        result = random.randint(lowerBound, upperBound)
        return result

if __name__ == "__main__":
    rand = Randomiser()
    for x in range(100):
        print rand.nextMove(1,4)