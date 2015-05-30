__author__ = 'Rob'

from math import log
from game import Game, Direction
from pybrain.rl.environments.episodic import EpisodicTask
from pybrain.utilities import Named
from copy import deepcopy

import numpy

class ai(object):

        def __init__(self, gameBoard):
            self.board = gameBoard

        # The following methods have been taken from 
        # https://github.com/Nicola17/term2048-AI

        def getColumn(self, col):
         return [self.board.get({"x":col, "y":i}) for i in range(self.board.size)]

        def getRow(self, row):
             return self.board.state[row]

        def validMove(self, board, direction):
            boardSizeAsRange = xrange(0, self.board.size)

            if direction == Direction.UP or direction == Direction.DOWN:
                for x in boardSizeAsRange:
                    col = self.getColumn(x)
                    for y in boardSizeAsRange:
                        if(y < self.board.size-1 and col[y] == col[y+1] and col[y]!=0):
                            return True
                        if(direction == Direction.UP and y > 0 and col[y] == 0 and col[y-1]!=0):
                            return True
                        if(direction == Direction.DOWN and y < self.board.size-1 and col[y] == 0 and col[y+1]!=0):
                            return True        
            
            if direction == Direction.LEFT or direction == Direction.RIGHT:
                for y in boardSizeAsRange:
                    row = self.getRow(y)
                    for x in boardSizeAsRange:
                        if(x < self.board.size-1 and row[x] == row[x+1] and row[x]!=0):
                            return True
                        if(direction == Direction.LEFT and x > 0 and row[x] == 0 and row[x-1]!=0):
                            return True
                        if(direction == Direction.RIGHT and x < self.board.size-1 and row[x] == 0 and row[x+1]!=0):
                            return True        
            return False

        def nextMove(self, recursion_depth=3):
            bestMove, bestScore = self.nextMoveRecur(self.board, recursion_depth, recursion_depth)
            return bestMove

        def nextMoveRecur(self, board, depth,maxDepth,base=0.9):
            bestScore = -1.
            bestMove = 0

            #print "My Best Score (Start): ", bestScore

            for m in range(1,5): # 1 to 4 (Game.Direction)
                if(self.validMove(self.board, m)):
                    newBoard = deepcopy(board)
                    newBoard.move(m)
                    score, tile = self.evaluate(newBoard)
                    #print "Evaluated Score: ", score


                    if depth != 0:
                        my_move, my_score = self.nextMoveRecur(newBoard,depth-1,maxDepth)

                        multiplier = pow(base,maxDepth-depth+1)

                        #print "My Best Score: ", my_score
                        #print "Multiplier: ", multiplier

                        score += my_score * multiplier
                        #print "Calculated Score: ", score

                    if(score > bestScore):
                        bestMove = m
                        bestScore = score

            #print "My Best Score (End): ", bestScore
            return bestMove, bestScore;

        
        def evaluate(self, board,commonRatio=0.25):
            linearWeightedVal = 0
            invert = False
            weight = 1.
            malus = 0
            criticalTile = (-1,-1)
            for y in range(0,board.size):
                for x in range(0,board.size):
                    b_x = x
                    b_y = y
                    if invert:
                        b_x = board.size - 1 - x
                    #linearW
                    currVal=board.get( {"x":b_x, "y":b_y} )
                    if(currVal == 0 and criticalTile == (-1,-1)):
                        criticalTile = (b_x,b_y)
                    linearWeightedVal += currVal*weight
                    weight *= commonRatio
                invert = not invert

            linearWeightedVal2 = 0
            invert = False
            weight = 1.
            malus = 0
            criticalTile2 = (-1,-1)
            for x in range(0,board.size):
                for y in range(0,board.size):
                    b_x = x
                    b_y = y
                    if invert:
                        b_y = board.size - 1 - y
                    #linearW
                    currVal=board.get( {"x":b_x, "y":b_y} )
                    if(currVal == 0 and criticalTile2 == (-1,-1)):
                        criticalTile2 = (b_x,b_y)
                    linearWeightedVal2 += currVal*weight
                    weight *= commonRatio
                invert = not invert


            linearWeightedVal3 = 0
            invert = False
            weight = 1.
            malus = 0
            criticalTile3 = (-1,-1)
            for y in range(0,board.size):
                for x in range(0,board.size):
                    b_x = x
                    b_y = board.size - 1 - y
                    if invert:
                        b_x = board.size - 1 - x
                    #linearW
                    currVal=board.get( {"x":b_x, "y":b_y} )
                    if(currVal == 0 and criticalTile3 == (-1,-1)):
                        criticalTile3 = (b_x,b_y)
                    linearWeightedVal3 += currVal*weight
                    weight *= commonRatio
                invert = not invert

            linearWeightedVal4 = 0
            invert = False
            weight = 1.
            malus = 0
            criticalTile4 = (-1,-1)
            for x in range(0,board.size):
                for y in range(0,board.size):
                    b_x = board.size - 1 - x
                    b_y = y
                    if invert:
                        b_y = board.size - 1 - y
                    #linearW
                    currVal=board.get( {"x":b_x, "y":b_y} )
                    if(currVal == 0 and criticalTile4 == (-1,-1)):
                        criticalTile4 = (b_x,b_y)
                    linearWeightedVal4 += currVal*weight
                    weight *= commonRatio
                invert = not invert


            linearWeightedVal5 = 0
            invert = True
            weight = 1.
            malus = 0
            criticalTile5 = (-1,-1)
            for y in range(0,board.size):
                for x in range(0,board.size):
                    b_x = x
                    b_y = y
                    if invert:
                        b_x = board.size - 1 - x
                    #linearW
                    currVal=board.get( {"x":b_x, "y":b_y} )
                    if(currVal == 0 and criticalTile5 == (-1,-1)):
                        criticalTile5 = (b_x,b_y)
                    linearWeightedVal5 += currVal*weight
                    weight *= commonRatio
                invert = not invert

            linearWeightedVal6 = 0
            invert = True
            weight = 1.
            malus = 0
            criticalTile6 = (-1,-1)
            for x in range(0,board.size):
                for y in range(0,board.size):
                    b_x = x
                    b_y = y
                    if invert:
                        b_y = board.size - 1 - y
                    #linearW
                    currVal=board.get( {"x":b_x, "y":b_y} )
                    if(currVal == 0 and criticalTile6 == (-1,-1)):
                        criticalTile6 = (b_x,b_y)
                    linearWeightedVal6 += currVal*weight
                    weight *= commonRatio
                invert = not invert


            linearWeightedVal7 = 0
            invert = True
            weight = 1.
            malus = 0
            criticalTile7 = (-1,-1)
            for y in range(0,board.size):
                for x in range(0,board.size):
                    b_x = x
                    b_y = board.size - 1 - y
                    if invert:
                        b_x = board.size - 1 - x
                    #linearW
                    currVal=board.get( {"x":b_x, "y":b_y} )
                    if(currVal == 0 and criticalTile7 == (-1,-1)):
                        criticalTile7 = (b_x,b_y)
                    linearWeightedVal7 += currVal*weight
                    weight *= commonRatio
                invert = not invert

            linearWeightedVal8 = 0
            invert = True
            weight = 1.
            malus = 0
            criticalTile8 = (-1,-1)
            for x in range(0,board.size):
                for y in range(0,board.size):
                    b_x = board.size - 1 - x
                    b_y = y
                    if invert:
                        b_y = board.size - 1 - y
                    #linearW
                    currVal=board.get( {"x":b_x, "y":b_y} )
                    if(currVal == 0 and criticalTile8 == (-1,-1)):
                        criticalTile8 = (b_x,b_y)
                    linearWeightedVal8 += currVal*weight
                    weight *= commonRatio
                invert = not invert

            maxVal = max(linearWeightedVal,linearWeightedVal2,linearWeightedVal3,linearWeightedVal4,linearWeightedVal5,linearWeightedVal6,linearWeightedVal7,linearWeightedVal8)
            if(linearWeightedVal2 > linearWeightedVal):
                linearWeightedVal = linearWeightedVal2
                criticalTile = criticalTile2
            if(linearWeightedVal3 > linearWeightedVal):
                linearWeightedVal = linearWeightedVal3
                criticalTile = criticalTile3
            if(linearWeightedVal4 > linearWeightedVal):
                linearWeightedVal = linearWeightedVal4
                criticalTile = criticalTile4
            if(linearWeightedVal5 > linearWeightedVal):
                linearWeightedVal = linearWeightedVal5
                criticalTile = criticalTile5
            if(linearWeightedVal6 > linearWeightedVal):
                linearWeightedVal = linearWeightedVal6
                criticalTile = criticalTile6
            if(linearWeightedVal7 > linearWeightedVal):
                linearWeightedVal = linearWeightedVal7
                criticalTile = criticalTile7
            if(linearWeightedVal8 > linearWeightedVal):
                linearWeightedVal = linearWeightedVal8
                criticalTile = criticalTile8

            #print "Max Value", maxVal
            #print "critical Tile", criticalTile
            return maxVal, criticalTile