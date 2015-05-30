from copy import deepcopy
from randomiser import *
import random

class MonteCarlo(object):

    def __init__(self):
        self.game = None
        self.gamesToPlay = 0


    def nextMove(self, game, gamesToPlay):
        '''
        Decide which direction to move in.
        Chosen direction will be between 1 and 4 (inclusive)
        '''

        # Update the game state
        self.game = game
        self.gamesToPlay = gamesToPlay

        # Generate the possible outcomes
        possibleOutcomes = []
        possibleMoves = [1,2,3,4]
        for move in possibleMoves:
            possibleOutcomes.append(self.playNGames(self.gamesToPlay))

        # Select the best outcome
        bestOutcome = max(possibleOutcomes)
        print 'Best Outcome: ', bestOutcome
        for move in possibleMoves:
            if possibleOutcomes[move-1] == bestOutcome:
                #print 'SELECTING MOVE: ', move
                return move


    def playNGames(self, numGames):
        results = []
        for game in range(numGames):
            endResult, score, maxBlock = self.playRandomGame()
            #print '  Game ', game, ' result: ', endResult, ' score: ', score, ' max block: ', maxBlock
            results.append(maxBlock)
        return sum(results) / len(results)

    def playRandomGame(self):
        rand = Randomiser()
        tempGame = deepcopy(self.game)
        while not tempGame.over:
            randomMove = rand.nextMove(1,4) # Make a random move
            tempGame.move(randomMove)

        if tempGame.won:
            return 'WIN', tempGame.score, tempGame.max_block
        else:
            return 'LOSE', tempGame.score, tempGame.max_block