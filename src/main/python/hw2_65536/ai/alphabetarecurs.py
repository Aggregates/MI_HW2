from hw2_65536.game import *
from math import *

class AlphaBetaRecursive(object):

    def __init__(self, game):
        self.game = game

    def nextMove(self, maxdepth):
        direction = 0
        bestscore = 0
        alpha = 0
        beta = -1000000

        best = abRecursive(self.game, maxdepth, alpha, beta)
        
        return best[0]
        
    def abRecursive(self, game, maxdepth, alpha, beta):
        best = (0,0)
        
        if self.game.over:
            if self.game.won:
                best[1] = 100000
            else:
                best[1] = min(self.game.score,1)
        elif depth == 0:
            best[1] = self.heuristicScore()
        else:
            for x in range(1,5): # Game.Direction
                tempGame = deepcopy(game)
                moved = tempGame.move(x)
                
                if moved==0:
                    continue

                tmp = self.nextMove(depth-1,0)
                
                if tmp[1] > alpha:
                    alpha = tmp[1]
                    best[0] = x
            best[1] = alpha

        return best[0]

    # calculate heuristic score based on game score, number of empty cells and clustering score
    def heuristicScore(self):
        score = self.game.score+(log(self.game.score*self.numberEmptyCells()))-self.clusterScore()
        return max(score,self.game.score)#ensure a positive result returned

    def clusterScore(self):
        clusterScore = 0
        neighbours = (-1, 0, 1)
        for i in range(5):
            for j in range(5):
                if self.game.state[i][j] == 0:
                    continue
                numOfNeighbours = 0
                sum = 0
                for k in neighbours:
                    x = i + k
                    if x < 0 or x > 5:
                        continue
                    for l in neighbours:
                        y = j + l
                        if y < 0 or y > 5:
                            continue
                        if self.game.state[x][y] > 0:
                            numOfNeighbours+=1
                            sum = abs(self.game.state[i][j]-self.game.state[x][y])

                clusterScore += sum/numOfNeighbours

        return clusterScore

    def numberEmptyCells(self):
        numberEmptyCells = 0
        available = self.game.get_available_cells()
        for x in range(available.__sizeof__()):
            if x==0:
                numberEmptyCells += 1
        return numberEmptyCells
