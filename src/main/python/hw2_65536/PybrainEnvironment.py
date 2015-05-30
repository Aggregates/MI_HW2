# Imports
from game import Game, Direction
from pybrain.rl.environments.episodic import EpisodicTask
from pybrain.utilities import Named
from math import log
from ai import *

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
        self.ai = MonteCarlo()
    
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
            #actionToSelect = self.alphaBeta(5, 1) #alphaBeta to choose best direction
            #actionToSelect = self.ai.nextMove(5,1)
            actionToSelect = self.ai.nextMove(self.game, 1)
            #print actionToSelect
            print 'ACTION TO SELECT: ', actionToSelect
            moved = self.game.move( self.action_list[actionToSelect - 1] )

            
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