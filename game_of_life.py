# Load libraries
import numpy as np

# Creating the current Generation
current_generation = np.array([['x','x','x','x'],['x',1,1,'x'],[1,'x',1,'x'],['x','x','x','x']]) # Xs are empty cells and 1s are live cells
current_generation # The generation has 4 live cells

# Creating  first next Generation of zeros.
'''Three out of four live cells die because they dont have immediate neighbors, one dead cell becomes alive 
because it is surrounded by 3 live cells
0 denotes a dead cell that was alive'''
next_generation_1 = current_generation[2,0] = 0 
next_generation_2 = next_generation[2,1] = 1
next_generation_1 = current_generation
next_generation_1 # The generation has 2 live cells and 3 dead cells
# Creating second next Generation of zeros
'''There are no live cells because the remaining two cells dont have any live neighbors'''
next_generation_2 = next_generation_1[1,2] = 0
next_generation_2 = next_generation_1[2,1] = 0
next_generation_2 = next_generation_1 
next_generation_2 # The generation has no live cells


