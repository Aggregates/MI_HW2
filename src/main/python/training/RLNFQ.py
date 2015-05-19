# Imports
from scipy import *
from hw2_65536.PybrainEnvironment import TwentyFortyEightEnvironment
from pybrain.rl.learners.valuebased import ActionValueNetwork
from pybrain.rl.agents import LearningAgent
from pybrain.rl.learners import NFQ, SARSA
from pybrain.rl.experiments import EpisodicExperiment
from pybrain.rl.environments import Task

import sys, time
import matplotlib.pyplot as plot

LEARNING_EPOCHS = 20 # Learning time
GAMES_PER_EPOCH = 25 # Batch size for Q Learner
GAMMA = 0.9

def train():

    # Make the environment
    environment = TwentyFortyEightEnvironment()

    # The task is the game this time
    task = environment

    # Make the reinforcement learning agent (use a network because inputs are continuous)
    network = ActionValueNetwork(task.nSenses, task.nActions)

    # Use Q learning for updating the table (NFQ is for networks)
    learner = NFQ()
    learner.gamma = GAMMA

    agent = LearningAgent(network, learner)

    # Set up an experiment
    experiment = EpisodicExperiment(task, agent)

    # Train the Learner
    meanScores = []
    for i in xrange(LEARNING_EPOCHS):
        experiment.doEpisodes(GAMES_PER_EPOCH)
        print "Iteration ", i, " With mean score ", task.meanScore
        meanScores.append(task.meanScore)
        agent.learn()
        agent.reset()

    params = {"learningEpochs": LEARNING_EPOCHS, "gamesPerEpoch": GAMES_PER_EPOCH, "gamma": GAMMA }
    return meanScores, params, agent