from pprint import pprint
import numpy as np
import matplotlib.pyplot as plt
import math
import time

def cubic_spline_interpolation(x, y):
    n = len(x)
    h = []
    a = []

    for i in range(n - 1):
        h.append(x[i + 1] - x[i])

    pprint(h)

    a.append(0)
    for i in range(1, n - 1):
        a.append(3 / h[i] * (y[i + 1] - y[i]) - 3 / h[i - 1] * (y[i] - y[i - 1]))

    pprint(a)

    l = [1]
    m = [0]
    z = [0]

    for i in range(1, n - 1):
        l.append(2 * (x[i + 1] - x[i - 1]) - h[i - 1] * m[i - 1])
        m.append(h[i] / l[i])
        z.append((a[i] - h[i - 1] * z[i - 1]) / l[i])

    pprint('l:' + str(l))

    pprint('m:' + str(m))

    pprint('z:' + str(z))

    l.append(1)
    z.append(0)

    c = [0] * (n - 1)
    b = [0] * (n - 1)
    d = [0] * (n - 1)
    c.append(0)

    for j in range(n - 2, -1, -1):
        c[j] = z[j] - m[j] * c[j + 1]
        b[j] = (y[j + 1] - y[j]) / h[j] - h[j] * (c[j + 1] + 2 * c[j]) / 3
        d[j] = (c[j + 1] - c[j]) / (3 * h[j])

    c.pop()

    pprint('a: ' + str(y))
    pprint('b: ' + str(b))
    pprint('c: ' + str(c))
    pprint('d: ' + str(d))

    return y, b, c, d


if __name__ == "__main__":
    #x = [10, 17, 24, 33, 47, 48, 59]
    #y = [22, 34,  78, 99, 23, 115, 119]

    x = [-2.0]
    y = []

    summ = -2.0

    for i in range(0, 8):
        summ += 0.5
        x.append(summ)

    for s in x:
        y.append(math.sin(5 * s) * 2.71828183**s)

    start_time = time.time()

    a, b, c, d = cubic_spline_interpolation(x, y)

    pprint("Execution time:" + str(time.time() - start_time))

    pprint(a)
    pprint(b)
    pprint(c)
    pprint(d)

    for i in range(0, len(x) - 1):
        xs = np.linspace(x[i], x[i + 1], 100)
        ys = []
        for j in xs:
            x_diff = j - x[i]
            ys.append(a[i] + b[i] * x_diff + c[i] * x_diff**2 + d[i] * x_diff**3)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.plot(xs, ys, color='red')

    plt.scatter(x, y, edgecolors='blue')

    plt.show()
