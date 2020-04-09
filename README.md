# ising
More proper Ising model simulation

## lattice
It's the main place of the ising model, we have to initialize it with a tuple of the shape of the lattice wich can be any dimension or size.
The lattice can by initialized with a randomized state (you can choose the ratio of up state) or all in 1 or -1 state.

### arguments:

- ##### shape:
>   type: tuple of int
>
>
>   the shape of the lattice is tested for 1 to 4 dimension

##### Optionnal:

- ##### all: 

>    type: **int** == 1 or -1
>
>    set the state at all 1 or -1 it overpass the r parrameter

- ##### r: 

>   type: **float** in [0, 1]
>
>   set a random state with a ratio r of 1 in the lattice (default r = 0.5)

- ##### adj: 

>   type: **numpy.array**
>
>   a vector of vector: is the representation of the spin interaction
>
>   |  0  |  J  |  0  |
>   | --- | --- | --- |
>   |**J**|**#**|**J**| 
>   |**0**|**J**|**0**| 
>
>   will be written as [[1,0],[-1,0],[0,1],[0,-1]]
>   
>   (as default it's the left right up down direct neighbor matrix will be genereted (whatever this mean in 4 or more dimensions))

- ##### J:

>   type: **numpy.array** or **float**
>
>   Is the interraction between spins, 
>   if J is an array he as to be the same length than adj 
>
>   (you can choose to make anisotropic iteractions !!)

- ##### B:
>   type **numpy.array** or **float**
>   is the magnetic field imposed on the lattice
>   if B is an array he as to have the same shape of the lattice 

        

## metropolis
Implementation of the Metropolis algorithm.
