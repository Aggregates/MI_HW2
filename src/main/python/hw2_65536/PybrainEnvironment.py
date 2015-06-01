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

#Enables printing of game states and realtime max blocks
VIS_DEBUG = 1

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
    maxRunBlock = 0
    minute = datetime.now().minute
    startTime = datetime.now()
    abDepth = 3
    moveCount = 0

    def __init__(self):
        self.nActions = len(self.action_list)
        self.reset()
        self.cumulativeReward = 0
        self.lastScore = 0
        self.meanScore = 0
        if GAME_TYPE==1:
            print "AI Type: AlphaBeta with SearchDepth=", self.abDepth
        elif GAME_TYPE==2:
            print "AI Type: MonteCarlo"
        elif GAME_TYPE==3:
            print "AI Type: Nicola"
        elif GAME_TYPE==4:
            print "AI Type: Randomiser"
        elif GAME_TYPE==5:
            print "AI Type: AlphaBetaRecursive with SearchDepth=", self.abDepth
            

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
            self.ai = Randomiser()
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
                actionToSelect = self.ai.nextMove(self.abDepth,1)
            elif GAME_TYPE==2:
                actionToSelect = self.ai.nextMove(self.game,1)
            elif GAME_TYPE==3:
                actionToSelect = self.ai.nextMove()
            elif GAME_TYPE==4:
                actionToSelect = self.ai.nextMove(1,4)
            elif GAME_TYPE==5:
                #if self.moveCount % 5 == 4:
                    #empty_cells = self.numberEmptyCells()
                    #new_depth = 2
                    #if empty_cells < 4:
                    #    self.timestamp()
                    #    self.printBoard("Limited Space")
                    #    new_depth = 7
                    #elif (empty_cells < 7):
                    #    new_depth = 5
                    #elif (empty_cells <= 10): # > =7
                    #    new_depth = 4
                    #elif (empty_cells < 15):# > 10
                    #    new_depth = 3
                    #elif (empty_cells < 20):# > 15
                    #    new_depth = 2
                    #
                    #if new_depth != self.abDepth:
                    #    self.abDepth = new_depth
                        #print "New Depth:", new_depth
                    
                actionToSelect = self.ai.nextMove(self.abDepth)
            self.moveCount += 1

            #print 'ACTION TO SELECT: ', actionToSelect
            moved = self.game.move( self.action_list[actionToSelect - 1] )
            
            #if(self.minute != datetime.now().minute and VIS_DEBUG == 0):
                #self.timestamp()
                #self.printBoard("Minute Update")    
                #self.minute = datetime.now().minute
                

            if(self.game.max_block > self.maxRunBlock and VIS_DEBUG ==1):
                self.maxRunBlock = self.game.max_block
                self.timestamp()
                print "Max Block:", self.maxRunBlock
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
        self.startTime = datetime.now()
        self.moveCount = 0
        self.maxRunBlock = 0
        #if(self.episode % 5 == 0):
        #    self.abDepth += 1
        #    print 'Seach Depth = ', self.abDepth
        
        
    def isFinished(self):
        if self.done > 200 or self.game.over or self.game.won and self.resetOnSuccess:
            if(VIS_DEBUG ==1):
                print ""
                self.timestamp()
                print "Final Score: ", self.game.score
                self.printBoard('End Game After ' + str(self.moveCount) + ' moves')
            if self.game.max_block > self.maxGameBlock:
                self.maxGameBlock = self.game.max_block
            if self.game.max_block > self.maxRunBlock:
                self.maxRunBlock = self.game.max_block
            self.lastScore = self.cumulativeReward
            self.meanScore = (0.99 * self.meanScore) + (0.01 * self.cumulativeReward)
            self.StartEpisode()
            return True
        return False
        
    def printBoard(self, message):
        print "----------------------- ", message, "  -------------------------------------"
        for i in range(5):
            print str(int(self.game.state[i][0])).ljust(7), str(int(self.game.state[i][1])).ljust(7), str(int(self.game.state[i][2])).ljust(7), str(int(self.game.state[i][3])).ljust(7), str(int(self.game.state[i][4])).ljust(7)
        print "----------------------- ", message, "  -------------------------------------"
        
    def timestamp(self):
        print ""
        now = datetime.now()
        time_d = now - self.startTime
        time_d_min = int(time_d.total_seconds() / 60)
        time_d_sec = int(time_d.total_seconds() % 60)
        print "     Time Elapsed: ", time_d_min, "min", time_d_sec,"sec"
        
        
    def numberEmptyCells(self):
        numberEmptyCells = 0
        for i in range(5):
            for j in range(5):
                if self.game.state[i][j]==0:
                    numberEmptyCells += 1
        return numberEmptyCells
