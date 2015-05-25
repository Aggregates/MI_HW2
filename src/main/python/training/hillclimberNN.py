# Imports
from scipy import *
from hw2_65536.PybrainEnvironment import TwentyFortyEightEnvironment
from pybrain.tools.shortcuts import buildNetwork
from pybrain.optimization import GA # HillClimber
from pybrain.rl.agents import OptimizationAgent
from pybrain.rl.experiments import EpisodicExperiment
from pybrain.rl.environments import Task

import sys, time
import matplotlib.pyplot as plot

# Constants
LEARNING_EPOCHS = 50 # Learning time
GAMES_PER_EPOCH = 50 # Batch size
HIDDEN_NODES = 30

def train():

    # Make the environment
    environment = TwentyFortyEightEnvironment()

    # Store the environment as the task
    task = environment

    # Set up the Neural Network
    neuralNet = buildNetwork(task.nSenses, HIDDEN_NODES, task.nActions)

    # Use a Genetic Algorithm as the Trainer
    trainer = GA( populationSize=20, topProportion=0.2, elitism=False
                , eliteProportion=0.25, mutationProb=0.1
                , mutationStdDev=0.2, tournament=False
                , tournamentSize=2 )

    agent = OptimizationAgent(neuralNet, trainer)

    # Set up an experiment
    experiment = EpisodicExperiment(task, agent)

    # Train the network
    meanScores = []
    for i in xrange(LEARNING_EPOCHS):
        print "Training Iteration", i
        experiment.doEpisodes(GAMES_PER_EPOCH)
        meanScores.append(task.meanScore)

    params = {"learningEpochs": LEARNING_EPOCHS, "gamesPerEpoch": GAMES_PER_EPOCH, "hiddenNodes": HIDDEN_NODES }
    return meanScores, params, experiment