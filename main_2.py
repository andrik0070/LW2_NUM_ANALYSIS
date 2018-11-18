from pprint import pprint
import numpy as np
import matplotlib.pyplot as plt


def TDMA(a, b, c, f):
    # a, b, c, f = map(lambda k_list: map(float, k_list), (a, b, c, f))

    alpha = [0]
    beta = [0]
    n = len(f)
    x = [0 for i in range(n)]

    for i in range(n - 1):
        alpha.append(-b[i] / (a[i] * alpha[i] + c[i]))
        beta.append((f[i] - a[i] * beta[i]) / (a[i] * alpha[i] + c[i]))

    x[n - 1] = (f[n - 1] - a[n - 2] * beta[n - 1]) / (c[n - 1] + a[n - 2] * alpha[n - 1])

    for i in reversed(range(n - 1)):
        x[i] = alpha[i + 1] * x[i + 1] + beta[i + 1]

    return x


def cubic_spline_interpolation(x, y):
    n = len(x)
    h = []
    a = []

    '''lower_diagonal = []
    middle_diagonal = []
    upper_diagonal = []'''

    for i in range(n - 1):
        h.append(x[i + 1] - x[i])

    pprint(h)

    a.append(0)
    for i in range(1, n - 1):
        a.append(3 / h[i] * (y[i + 1] - y[i]) - 3 / h[i - 1] * (y[i] - y[i - 1]))

    pprint(a)

    '''for i in range(len(x) - 2):
        lower_diagonal.append(h[i])
    lower_diagonal.append(0.0)

    middle_diagonal.append(1.0)
    for i in range(2, len(x)):
        middle_diagonal.append(2.0 * (h[i - 2] + h[i - 1]))
    middle_diagonal.append(1.0)

    upper_diagonal.append(0.0)
    for i in range(1, len(x) - 1):
        upper_diagonal.append(h[i])

    pprint(len(lower_diagonal))
    pprint(len(middle_diagonal))
    pprint(len(upper_diagonal))
    pprint(len(a))

    pprint(TDMA(lower_diagonal, middle_diagonal, upper_diagonal, a))'''

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
    x = [1, 2, 3, 4, 5, 6, 7]
    y = [1, 7, 15, 21, 46, 79, 110]

    a, b, c, d = cubic_spline_interpolation(x, y)

    pprint(len(a))
    pprint(len(b))
    pprint(len(c))
    pprint(len(d))

    for i in range(0, len(x) - 1):
        xs = np.linspace(x[i], x[i + 1], 100)
        ys = []
        for j in xs:
            x_diff = j - x[i]
            ys.append(a[i] + b[i] * x_diff + c[i] * x_diff**2 + d[i] * x_diff**3)
            plt.plot(xs, ys, color='red')

    plt.show()


