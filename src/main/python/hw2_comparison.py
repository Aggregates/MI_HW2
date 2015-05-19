# Imports
from training import hillclimberNN, RLNFQ
from os import path, makedirs
from time import strftime, time

import pickle
import matplotlib.pyplot as plot

def run():
    trainer = "RLNFQ"
    meanScores, params, network = RLNFQ.train()

     # Create the output path if it doesn't exist
    generated_dir = path.abspath(path.join("generated", "{}-{}".format(trainer, strftime("%Y-%m-%d_%H-%M-%S")) ))
    if not path.exists(generated_dir):
        makedirs(generated_dir)

    # save parameters
    with open(path.normpath(path.join(generated_dir, "params.txt")), "a") as f:
        for key in params.keys():
            f.write("{} = {}\n".format(key, params[key]))

    # Save the Trained Neural Network
    uniqueFileName = path.normpath(path.join(generated_dir, "data.pkl"))
    writeMode = 'wb' # Write Bytes
    pickle.dump(network, open(uniqueFileName, writeMode))

    # Show the mean scores
    plot.plot(meanScores)
    plot.title("Mean Agent Score Per Last 100 Games")
    plot.show()

if __name__ == "__main__":
    run();