import numpy as np
 
a = np.matrix([[1, 5, -5], [4, 0, 3], [2, -10, 3]])
 
print("Визначник: {}".format(np.linalg.det(a)))
