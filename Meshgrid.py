import numpy as np
l = np.linspace(0, 5, 6)
print(l)
k = np.linspace(-5, 0, 6)
print(k)
x1, y1 = np.meshgrid([1,2,3], [5,6,7], sparse = False)
print("x1 is : ")
print(x1)
print("y1 is : ")
print(y1)