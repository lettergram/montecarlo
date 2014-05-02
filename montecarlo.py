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
        sum += func(x[i], y[i])
        print(i, sum / (i+1))


    area = abs(xmax - xmin) * abs(ymax - ymin)
    return area * (sum / n)

total1 = monte(func1, 10000, 1, 5, 1, 5)
total2 = monte(func2, 10000, 1, 3, 1, 2)

print(total1, total2)
