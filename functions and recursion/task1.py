from math import sqrt

def getDistance(x_1, y_1, x_2, y_2):
    return sqrt((x_2 - x_1)**2 + (y_2 - y_1)**2)

x_1 = float(input())
y_1 = float(input())
x_2 = float(input())
y_2 = float(input())
print(getDistance(x_1, y_1, x_2, y_2))