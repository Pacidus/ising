from ising.metropolis import algorithm
import matplotlib.pyplot as plt
import numpy as np

plt.ion()

adj = np.array([[i,j] for i in range(-10,11) for j in range(-10,11) if (i*i+j*j) <= 25 and (i*i+j*j) != 0])
J = np.array([1/(i*i).sum() for i in adj])
J /= J.sum()
J *= 4

Ising = algorithm((100,100), adj = adj, J = J, B = 0.01, beta = 90)
Ising.beta = 1

lattice = Ising.get_state

img = plt.imshow(lattice())
for i in range(20000):
    Ising.step(100)
    if 0 == i%100:
        img.set_data(lattice())
        plt.pause(1/60)
