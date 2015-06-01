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
            possibleOutcomes.append(self.playNGames(self.gamesToPlay, move))

        # Select the best outcome
        bestOutcome = max(possibleOutcomes)
        for move in possibleMoves:
            if possibleOutcomes[move-1] == bestOutcome:
                return move


    def playNGames(self, numGames, startMove):
        '''
        Plays n games of a particular game. It starts
        by making the first move and then calculated the
        expected long term behaviour of the state of
        the game, after randomly choosing moves after
        the initial move, in order to evaluate the
        effectiveness of the initial move
        '''
        results = []
        for game in range(numGames):
            # Create a copy of the game state
            tempGame = deepcopy(self.game)

            # Make the first move
            tempGame.move(startMove)

            # Play randomly until completion
            endResult, score, maxBlock = self.playRandomGame(tempGame)
            results.append(score)
        averageScore = sum(results) / len(results)
        return averageScore

    def playRandomGame(self, tempGame):
        '''
        Uses the Randomiser AI to randomly select moves from the
        available moveset in order to evaluate the effectiveness
        of a game state after an initial move is selected
        '''
        rand = Randomiser()
        while not tempGame.over:
            randomMove = rand.nextMove(1,4) # Make a random move
            tempGame.move(randomMove)

        if tempGame.won:
            return 'WIN', tempGame.score, tempGame.max_block
        else:
            return 'LOSE', tempGame.score, tempGame.max_block