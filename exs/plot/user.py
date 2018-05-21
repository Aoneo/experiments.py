#import f.py
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D, plot3d
import numpy as np
import time

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

def f(x):
    return x**3 // math.sqrt(2)**2

def f3d(x,y):
    return math.sin(10*(x**2 + y**2))/10


def generatePoints(a, b, n):
    pointsX = []
    pointsY = []
    n = int(n)
    x = a
    step = (abs(a) + abs(b)) / n
    for i in range(n + 1):
        pointsX.append(x)
        pointsY.append(f(x))
        x += step
        
    return pointsX, pointsY

def generate3D(x, y, a, b, s):
    pointsX = []
    pointsY = []
    pointsZ = []
    s = int(s)
    step = (abs(a) + abs(b)) / s
    for i in range(s + 1):
        pointsX.append(f3d(x,y))
        pointsY.append(f3d(x,y))
        pointsZ.append(f3d(x,y))
        x += step
    return pointsX,pointsY,pointsZ

x,y,z = generate3D(1.1, math.sqrt(2), 0, 100, 100)
print(x,y)
print(z)

Axes3D.plot_surface(x,y,z)
plt.show()
