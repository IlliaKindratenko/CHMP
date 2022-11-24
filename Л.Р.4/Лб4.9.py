import numpy as np 
a = np.matrix([[3, 2, 1], [2, -1, 1], [1, 5, 0]])
b = np.matrix([[-2], [-1], [0]]) 
x = np.linalg.solve(a, b) 
print(x)
