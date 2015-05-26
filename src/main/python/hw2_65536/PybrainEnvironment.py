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
            for i in xrange(4):
                actionToSelect = (int(action[0]) + i ) % 4 #alphaBeta to choose best direction
                moved = self.game.move( self.action_list[actionToSelect] )
                if moved:
                    break
            
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

    def alphaBeta(self, state, depth, max, min, player):
        direction = 0
        bestscore = 0
        state = self.game.state
        #if self.isFinished():

        if depth==0:
            bestscore = self.heuristicScore()

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