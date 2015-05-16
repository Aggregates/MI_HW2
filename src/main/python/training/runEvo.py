
#import the RL libraries
from scipy import *
import sys, time

from PybrainEnvironment import TwentyFortyEightEnvironment
from pybrain.tools.shortcuts import buildNetwork
from pybrain.optimization import GA #HillClimber
from pybrain.rl.agents import OptimizationAgent
from pybrain.rl.experiments import EpisodicExperiment
from pybrain.rl.environments import Task

#set the learning time
learning_eps = 30

#set the batch size
games_per_ep = 50


# make the environment
environment = TwentyFortyEightEnvironment()

#the task is the game this time
task = environment

#create our neural network
controller = buildNetwork(task.nsenses, 30, task.nactions)

#use a Genetic Algorithm
#all the commented out lines are options you can play with
learner = GA(populationSize=20
            , topProportion=0.2
            , elitism=False
            , eliteProportion=0.25
            , mutationProb=0.1
            , mutationStdDev=0.2
            , tournament=False
            , tournamentSize=2
            )

agent = OptimizationAgent(controller, learner)



#set up an experiment
experiment = EpisodicExperiment(task, agent)

meanscores = []
for i in xrange(learning_eps):
    print i
    experiment.doEpisodes(games_per_ep)
    meanscores.append(task.meanscore)

import matplotlib.pyplot as plt
plt.plot(meanscores)

plt.title("Mean Agent Score Per Last 100 Games")
plt.show()




