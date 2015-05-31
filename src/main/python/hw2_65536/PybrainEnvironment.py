# Imports
from game import Game, Direction
from pybrain.rl.environments.episodic import EpisodicTask
from pybrain.utilities import Named
from math import log
from ai import *
from datetime import datetime

import numpy

#Game types - 1=AlphaBeta, 2=MonteCarlo, 3=Nicola, 4=Randomiser, 5=AlphaBetaRecursive
GAME_TYPE = 5

class TwentyFortyEightEnvironment(EpisodicTask, Named):

    # The number of actions
    action_list = (Direction.LEFT,Direction.RIGHT,Direction.UP,Direction.DOWN)
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
    minute = datetime.now().minute

    def __init__(self):
        self.nActions = len(self.action_list)
        self.reset()
        self.cumulativeReward = 0
        self.lastScore = 0
        self.meanScore = 0
        if GAME_TYPE==1:
            print "AI Type: AlphaBeta"
        elif GAME_TYPE==2:
            print "AI Type: MonteCarlo"
        elif GAME_TYPE==3:
            print "AI Type: Nicola"
        elif GAME_TYPE==4:
            print "AI Type: Randomizer"
        elif GAME_TYPE==5:
            print "AI Type: AlphaBetaRecursive"

    def reset(self):
        self.game = Game()
        self.done = 0
        self.startState = self.game.state
        if GAME_TYPE==1:
            self.ai = AlphaBeta(self.game)
        elif GAME_TYPE==2:
            self.ai = MonteCarlo()
        elif GAME_TYPE==3:
            self.ai = Nicola(self.game)
        elif GAME_TYPE==4:
            self.ai = Randomizer()
        elif GAME_TYPE==5:
            self.ai = AlphaBetaRecursive(self.game)
    
    
    def getObservation(self):
        return self.game.state.flatten()
        
    def performAction(self, action):
        if len(action) == 4:
            action = numpy.argsort(action)
        
        if self.game.won or self.game.over:
            self.done += 1            
        else:
            lastgs = self.game.score
            
            # Try all possible moves
            # Alpha-Beta or Minimax goes here to choose a better move rather than just the first one it can.
            if GAME_TYPE==1:
                actionToSelect = self.ai.nextMove(5,1)
            elif GAME_TYPE==2:
                actionToSelect = self.ai.nextMove(self.game,1)
            elif GAME_TYPE==3:
                actionToSelect = self.ai.nextMove()
            elif GAME_TYPE==4:
                actionToSelect = self.ai.nextMove(1,4)
            elif GAME_TYPE==5:
                actionToSelect = self.ai.nextMove(2)
                
            #print actionToSelect
            #print 'ACTION TO SELECT: ', actionToSelect
            moved = self.game.move( self.action_list[actionToSelect - 1] )
            
            if(self.minute != datetime.now().minute):
                self.printBoard()
                self.minute = datetime.now().minute

            if(self.game.max_block > self.maxGameBlock):
                self.maxGameBlock = self.game.max_block
                print "Max Block:", self.maxGameBlock
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
        if self.done > 20 or self.game.over or self.game.won and self.resetOnSuccess:
            if self.game.max_block > self.maxGameBlock:
                self.maxGameBlock = self.game.max_block
            self.lastScore = self.cumulativeReward
            self.meanScore = (0.99 * self.meanScore) + (0.01 * self.cumulativeReward)
            self.StartEpisode()
            return True
        return False
    def printBoard(self):
        for i in range(5):
            print str(int(self.game.state[i][0])).ljust(7), str(int(self.game.state[i][1])).ljust(7), str(int(self.game.state[i][2])).ljust(7), str(int(self.game.state[i][3])).ljust(7), str(int(self.game.state[i][4])).ljust(7)
                