# Interpret all numbers as coordinate pairs (x, y). Then all points
# will be in the square with area 1. If we count all points in the square
# and then in the quarter of circle, their ratio we will tend to pi / 4.

import random as rd

def random_pi(N):
    x = 0
    y = 0
    circle_points = 0
    total_points = 0
    for i in range(1, N // 2):
        x = rd.random()
        y = rd.random()
        if (x**2 + y**2 <= 1):
            circle_points += 1
        total_points += 1
    return 4 * circle_points / total_points
