from ising.metropolis import algorithm
import matplotlib.pyplot as plt
import numpy as np

plt.ion()

Ising = algorithm((100,100))
Ising.beta = 50

lattice = Ising.get_state

img = plt.imshow(lattice())

for i in range(20000):
    Ising.step(100)
    if 0 == i%100:
        img.set_data(lattice())
        plt.pause(1/60)
