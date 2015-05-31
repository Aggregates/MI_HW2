from hw2_65536.game import *
from math import *
from copy import deepcopy
from collections import namedtuple

class AlphaBetaRecursive(object):

    def __init__(self, game):
        self.game = game

    def nextMove(self, maxdepth):
        alpha = 0
        beta = -1000000

        direction = self.abRecursive(self.game,maxdepth, maxdepth, alpha, beta)
        
        return direction
        
    def abRecursive(self, game, depth, maxdepth, alpha, beta):
        bestscore = 0
        bestdirection = 1
        
        if game.over:
            if game.won:
                bestscore = 100000
            else:
                bestscore = min(game.score,1)
        elif depth == 0:
            bestscore = self.heuristicScore(game)
        else:
            for x in range(1,5): # Game.Direction
                tempGame = deepcopy(game)
                moved = tempGame.move(x)
                
                if moved==0:
                    continue

                tmp = self.abRecursive(tempGame, depth-1, maxdepth, alpha, beta)
                
                if (tmp > alpha):
                    alpha = tmp
                    bestdirection = x
            bestscore = alpha
        if depth==maxdepth:
            return bestdirection
        else:
            return bestscore

    # calculate heuristic score based on game score, number of empty cells and clustering score
    def heuristicScore(self, game):
        if(game.score == 0):
            return 0
        score = game.score + log(game.score * self.numberEmptyCells(game)) - self.clusterScore(game)
        
        return max(score,game.score) #ensure a positive result returned

    def clusterScore(self, game):
        clusterScore = 0
        neighbours = (-1, 0, 1)
        for i in range(5):
            for j in range(5):
                if game.state[i][j] == 0:
                    continue
                numOfNeighbours = 0
                sum = 0
                for k in neighbours:
                    x = i + k
                    if x < 0 or x >= 5:
                        continue
                    for l in neighbours:
                        y = j + l
                        if y < 0 or y >= 5:
                            continue
                        if game.state[x][y] > 0:
                            numOfNeighbours+=1
                            sum = abs(game.state[i][j]-game.state[x][y])

                clusterScore += sum/numOfNeighbours

        return clusterScore

    def numberEmptyCells(self, game):
        numberEmptyCells = 0
        available = game.get_available_cells()
        for x in range(available.__sizeof__()):
            if x==0:
                numberEmptyCells += 1
        return numberEmptyCells
