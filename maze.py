import numpy as np
import random
n = 1
p = random.uniform(0,1)
size = 6
grid = np.random.binomial(n,p, size=(size,size))
first_row = grid[0]
first_row[first_row == 1] = False
grid[0] = first_row
for i in range(1,size):
	grid[i,size-1] = 1
def carve_maze(grid, size):
	output_grid = np.empty([size*3, size*3])
	output_grid[:] = 1
	i = 0
	j = 0
	while i < size:
		w = i*3 + 1
		while j < size:
			k = j*3 + 1
			toss = grid[i,j]
			output_grid[w,k] = False
			if toss == 0 and k+2 < size*3:
				output_grid[w,k+1] = False
				output_grid[w,k+2] = False
			if toss == 1 and w-2 >=0:
				output_grid[w-1,k] = False
				output_grid[w-2,k] = False
			j = j + 1
		i = i + 1
		j = 0
	
	return output_grid

