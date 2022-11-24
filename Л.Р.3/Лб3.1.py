import numpy as np
import math
from scipy.misc import derivative
a = int(input("введіть а: ")) 
b = int(input("введіть b: ")) 
e = float(input("введіть e(точність): ")) 
def f(x):
    return  pow(x,4)-108*x+7
if (f(b)*derivative(f, b, n = 2)>0):
    xi = b
else:
    xi = a
df = derivative(f,xi, n= 1)
xi_1 = xi - f(xi)/df
while (abs(xi_1 - xi) > e):
    xi = xi_1
    xi_1 = xi - f(xi)/df
print ("x = {}".format(xi_1))