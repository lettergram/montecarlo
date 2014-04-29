import numpy as np

def func(x, y):
    return x*x + x*y + y*y

def monte(n, ymin, ymax, xmin, xmax):

    sum = 0
    x = np.random.uniform(ymin, ymax, n)
    y = np.random.uniform(xmin, xmax, n)
    for i in range(n):
        sum += func(x[i], y[i])
        print(i, (2 * sum)/(i+1))
    return (2 * sum) / n

print monte(10000, 0, 1, 2, 4);
