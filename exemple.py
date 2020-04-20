from isingm.metropolis import algorithm
import matplotlib.pyplot as plt
import numpy as np

plt.ion()

adj = np.array([[i,j] for i in range(-10,11) for j in range(-10,11) if (i*i+j*j) <= 25 and (i*i+j*j) != 0])
J = np.array([1/(i*i).sum() for i in adj])
J /= J.sum()
J *= -4

Ising = algorithm((300,300), adj = adj, J = J, B = 1.0, beta = 90)
Ising.beta = 10

lattice = Ising.get_state

fig = plt.figure()
img = plt.imshow(lattice())
for i in range(40000):
    
    j = 0
    while j < 100:
        Ising.step(100)
        j += 1
    img.set_data(lattice())

    fig.canvas.draw()
    fig.canvas.flush_events()     
