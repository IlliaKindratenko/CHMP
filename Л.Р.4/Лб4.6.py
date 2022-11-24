import numpy as np
 
a = np.matrix([[1, 1, 1, 1], [1, 1, -1, -1], [1, -1, 1, -1], [1, -1, -1, 1]])
 
b = np.linalg.inv(a)
 
print("Обернена матриця: \n{}".format(b))
