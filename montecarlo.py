import numpy as np

def func1(x, y):
    return x*x + x*y + y*y

def func2(y, x):
    return x**3 + y**3 + y*x**2 + y**2 + 2

def monte(func, n, ymin, ymax, xmin, xmax):

    sum = 0
    x = np.random.uniform(xmin, xmax, n)
    y = np.random.uniform(ymin, ymax, n)

    for i in range(n):
        sum += 2 * func(x[i], y[i])
        print(i, sum / (i+1))

    return sum / n

total1 = monte(func1, 30000, 0, 1, 2, 4)
total2 = monte(func2, 30000, 1, 3, 1, 2)

print(total1, total2)
