This is the main place of the Ising model,
we have to initialize it with a tuple of the lattice shape that can be of any dimension or size.
The lattice can be initialized with a random state (you can choose the state ratio up) or all in a state 1 or -1.

### arguments:

- ##### shape:

>   type: **tuple(int)**
>
>   The shape of the lattice is tested for 1 to 4 dimension.
>   Every values of shape must be > 0 

#### Optionnal:

- ##### all:

>    type: **int** == 1 or -1
>
>    Set the state at all 1 or -1 it overpass the r parrameter.

- ##### r: 

>   type: **float** in [0, ..., 1]
>
>  Set a random state with a ratio r of 1 in the lattice (default r = 0.5).

- ##### adj: 

>   type: **numpy.array**
>
>   A vector of vector: is the representation of the spin interaction.
>
>   |  0  |  J  |  0  |
>   | --- | --- | --- |
>   |**J**|**#**|**J**| 
>   |**0**|**J**|**0**| 
>
>   Will be written as [[1,0],[-1,0],[0,1],[0,-1]]
>   
>   As default it's the left right up down direct neighbor matrix will be genereted (whatever this mean in 4 or more dimensions).

- ##### J:

>   type: **numpy.array** or **float**
>
>   Is the interraction between spins, 
>   if J is an array he as to be the same length than adj.
>
>   (you can choose to make anisotropic iteractions !!)

- ##### B:

>   type: **numpy.array** or **float**
>
>   Is the magnetic field imposed on the lattice,
>   if B is an array he as to have the same shape of the lattice

- ##### beta:

>   type: **float**
>
>   Beta is 1/(Kb * T) with T the absolute temp,
>   and Kb is the Boltzmann constant.
