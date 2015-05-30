import random

class MonteCarlo(object):

    def nextMove():
        '''
        Decide which direction to move in.
        Chosen direction will be between 1 and 4 (inclusive)
        '''

        direction = random.randint(1,4)
        return direction

if __name__ == "__main__":
    print nextMove()
