# Imports
from training import hillclimberNN, RLNFQ
from os import path, makedirs
from time import strftime, time

import pickle
import matplotlib.pyplot as plot

def run():
    trainer1 = "RLNFQ"
    meanScores1, params1, network = RLNFQ.train()
    trainer2 = "HillclimberNN"
    meanScores2, params2, experiment2 = hillclimberNN.train()

     # Create the output path if it doesn't exist
    generated_dir1 = path.abspath(path.join("generated", "{}-{}".format(trainer1, strftime("%Y-%m-%d_%H-%M-%S")) ))
    generated_dir2 = path.abspath(path.join("generated", "{}-{}".format(trainer2, strftime("%Y-%m-%d_%H-%M-%S")) ))
    if not path.exists(generated_dir1):
        makedirs(generated_dir1)
    if not path.exists(generated_dir2):
        makedirs(generated_dir2)

    # save parameters
    with open(path.normpath(path.join(generated_dir1, "params1.txt")), "a") as f:
        for key in params1.keys():
            f.write("{} = {}\n".format(key, params1[key]))

    with open(path.normpath(path.join(generated_dir2, "params2.txt")), "a") as f:
        for key in params2.keys():
            f.write("{} = {}\n".format(key, params2[key]))

    # Save the Trained Neural Network
    uniqueFileName = path.normpath(path.join(generated_dir1, "data.pkl"))
    writeMode = 'wb' # Write Bytes
    pickle.dump(network, open(uniqueFileName, writeMode))

    uniqueFileName = path.normpath(path.join(generated_dir2, "data.pkl"))
    writeMode = 'wb' # Write Bytes
    pickle.dump(network, open(uniqueFileName, writeMode))

    # Show the mean scores
    plot.plot(meanScores1)
    plot.plot(meanScores2)
    plot.title("Mean Agent Score Per Last 100 Games")
    plot.show()

if __name__ == "__main__":
    run()