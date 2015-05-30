# Imports
from game import Game, Direction
from pybrain.rl.environments.episodic import EpisodicTask
from pybrain.utilities import Named
from math import log


import numpy

class TwentyFortyEightEnvironment(EpisodicTask, Named):

    # The number of actions
    action_list = ( Direction.UP, Direction.LEFT, Direction.DOWN, Direction.RIGHT )
    nActions = len(action_list) # 4
    
    nSenses = 5 * 5
    inDimensions = nSenses
    outDimensions = nActions
    steps = 0 # Number of steps of the current trial
    episode = 0 # Number of the current episode
    resetOnSuccess = True
    done = 0
    game = None
    maxGameBlock = 0

    def __init__(self):
        self.nActions = len(self.action_list)
        self.reset()
        self.cumulativeReward = 0
        self.lastScore = 0
        self.meanScore = 0

    def reset(self):
        self.game = Game()
        self.done = 0
        self.startState = self.game.state
    
    def getObservation(self):
        return self.game.state.flatten()
        
    def performAction(self, action):
        if len(action) == 4:
            action = numpy.argsort(action)
        
        if self.game.won or self.done:
            self.done += 1            
        else:
            lastgs = self.game.score
            
            # Try all possible moves
            # Alpha-Beta or Minimax goes here to choose a better move rather than just the first one it can.
            actionToSelect = self.alphaBeta(5, 1) #alphaBeta to choose best direction
            #actionToSelect = self.nextMove()
            moved = self.game.move( self.action_list[actionToSelect] )

            
            if not moved or self.game.won:
                self.r = moved * -2.0
                self.done += 1
            else:
                self.r = self.game.score - lastgs
            self.cumulativeReward += self.r
            
    def getReward(self):
        return self.r    

    def GetInitialState(self):
        self.StartEpisode()
        return getObservation()
        
    def StartEpisode(self):
        self.reset()
        self.steps = 0
        self.cumulativeReward = 0
        self.episode = self.episode + 1
        self.done = 0
        
    def isFinished(self):
        if self.done > 2 or self.game.won and self.resetOnSuccess:
            if self.game.max_block > self.maxGameBlock:
                self.maxGameBlock = self.game.max_block
            self.lastScore = self.cumulativeReward
            self.meanScore = (0.99 * self.meanScore) + (0.01 * self.cumulativeReward)
            self.StartEpisode()
            return True
        return False

    def nextMove(self, recursion_depth=3):
        m,s = self.nextMoveRecur(recursion_depth,recursion_depth)
        return m

    def alphaBeta(self, depth, player):
        direction = 0
        bestscore = 0
        alpha = 1000000
        beta = -1000000
        if self.isFinished():
            if self.game.won:
                bestscore = 100000
            else:
                bestscore = min(self.game.score,1)
        elif depth==0:
            bestscore = self.heuristicScore()
        else:
            if player==1:
                for x in self.action_list:
                    self.tempState = self.game
                    self.tempState.move(x)
                    points = self.tempState.score
                    if (points==0) and (self.tempState==self.game):
                        continue
                    currentResult = self.alphaBeta(depth-1,0)

            #else:

        return direction

    # calculate heuristic score based on game score, number of empty cells and clustering score
    def heuristicScore(self):
        score = self.game.score+(log(self.game.score*self.noEmptyCells()))-self.clusterScore()
        return max(score,self.game.score)#ensure a positive result returned

    def clusterScore(self):
        clusterScore = 0

        return clusterScore

    def noEmptyCells(self):
        noEmptyCells = 0
        available = self.game.get_available_cells()
        for x in range(available.__sizeof__()):
            if x==0:
                noEmptyCells=noEmptyCells+1
        return noEmptyCells