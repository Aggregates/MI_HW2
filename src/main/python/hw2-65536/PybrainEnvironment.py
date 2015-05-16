from game import Game,Direction
from pybrain.rl.environments.episodic import EpisodicTask
import numpy
from pybrain.utilities import Named

class TwentyFortyEightEnvironment(EpisodicTask,Named):

    #The number of actions.
    action_list = (Direction.up,Direction.left,Direction.down,Direction.right)
    nactions = len(action_list)
    
    nsenses = 5*5
    indims = nsenses
    outdims = nactions

    # number of steps of the current trial
    steps = 0

    # number of the current episode
    episode = 0
    
    resetOnSuccess = True
    
    done = 0
    
    game = None

    def __init__(self):
        self.nactions = len(self.action_list)
        self.reset()
        self.cumreward = 0
        self.lastscore = 0
        self.meanscore = 0

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
            
            #try all possible moves
            for i in xrange(4):
                moved = self.game.move(self.action_list[((int(action[0])+i)%4)])
                if moved:
                    break
            
            if not moved or self.game.won:
                self.r = moved*-2.0
                self.done += 1
            else:
                self.r = self.game.score - lastgs
            self.cumreward += self.r
            
    def getReward(self):
        return self.r    

    def GetInitialState(self):
        self.StartEpisode()
        return getObservation()
        
        
    def StartEpisode(self):
        self.reset()
        self.steps = 0
        self.cumreward = 0
        self.episode = self.episode + 1
        self.done = 0
        
    def isFinished(self):
        if self.done > 2 or self.game.won and self.resetOnSuccess:
            self.lastscore = self.cumreward
            self.meanscore = 0.99*self.meanscore + 0.01*self.cumreward
            self.StartEpisode()
            return True
        return False
