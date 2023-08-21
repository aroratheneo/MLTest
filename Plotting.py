import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt

def f(x, y):
    return (x ** 2 + y ** 2)

x = np.linspace(-6, 6, 30)
y = np.linspace(-6, 6, 30)

X, Y = np.meshgrid(x, y)
Z = f(X, Y)

# plot1 = plt.subplot2grid((3, 3), (0, 0), colspan=2)
# plot2 = plt.subplot2grid((3, 3), (0, 2), rowspan=3, colspan=2)
# plot3 = plt.subplot2grid((3, 3), (1, 0), rowspan=2)


# axis[0, 0].plot(X, Y1)

fig = plt.figure()
ax = fig.add_subplot(2, 2, 1,projection='3d')
# ax = plt.axes(projection='3d')
# ax.contour3D(X, Y, Z, 50, cmap='binary')
ax.plot_surface(X, Y, Z, cmap="viridis",edgecolor='none')

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
# plt.show()

ax2 = fig.add_subplot(2, 2, 2)

ax2.contour(X, Y, Z, colors='black');

ax3 = fig.add_subplot(2, 2, 3 ,projection='3d')

ax3.contour3D(X, Y, Z, 50, cmap='binary')

plt.show()