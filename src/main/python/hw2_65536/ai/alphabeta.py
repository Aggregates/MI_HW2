from hw2_65536.game import *

class AlphaBeta(object):

    def __init__(self, game):
        self.game = game

    def nextMove(self, depth, numPlayers):
        direction = 0
        bestscore = 0
        alpha = 1000000
        beta = -1000000

        if self.game.over:
            if self.game.won:
                bestscore = 100000
            else:
                bestscore = min(self.game.score,1)
        elif depth == 0:
            bestscore = self.heuristicScore()
        else:
            if numPlayers == 1:
                for x in range(1,4): # Game.Direction
                    self.tempState = self.game
                    self.tempState.move(x)
                    
                    # Calculate the points from move and see if we got any
                    points = self.tempState.score
                    if (points==0) and (self.tempState==self.game):
                        continue

                    currentResult = self.nextMove(depth-1,0)


        return direction

    # calculate heuristic score based on game score, number of empty cells and clustering score
    def heuristicScore(self):
        score = self.game.score+(log(self.game.score*self.numberEmptyCells()))-self.clusterScore()
        return max(score,self.game.score)#ensure a positive result returned

    def clusterScore(self):
        clusterScore = 0

        return clusterScore

    def numberEmptyCells(self):
        numberEmptyCells = 0
        available = self.game.get_available_cells()
        for x in range(available.__sizeof__()):
            if x==0:
                numberEmptyCells += 1
        return numberEmptyCells