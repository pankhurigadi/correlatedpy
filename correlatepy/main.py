import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import random
import quantecon as qe
from tqdm.notebook import tqdm
from collections import Counter


## Chicken game
epsilon = 0.02
history = [(0,0)]

P0 = Player(0, [0, 1], np.array([[0, 7], [2, 6]]), history, epsilon)
P1 = Player(1, [0, 1], np.array([[0, 2], [7, 6]]), history, epsilon)

G = Game(history, epsilon)

G.add_player(P0)
G.add_player(P1)

G.runGame()
