from pprint import pprint


def TDMA(a, b, c, f):
    #a, b, c, f = map(lambda k_list: map(float, k_list), (a, b, c, f))

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
    h = []
    a = []
    lower_diagonal = []
    middle_diagonal = []
    upper_diagonal = []

    for i in range(len(x) - 1):
        h.append(x[i + 1] - x[i])

    a.append(0.0)
    for i in range(1, len(x) - 1):
        a.append(3 / h[i] * (y[i + 1] - y[i]) - 3 / h[i - 1] * (y[i] - y[i - 1]))
    a.append(0.0)

    for i in range(len(x) - 2):
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

    pprint(TDMA(lower_diagonal, middle_diagonal, upper_diagonal, a))


if __name__ == "__main__":
    cubic_spline_interpolation([1, 2, 3, 4, 5, 6, 7], [1, 4, 9, 16, 25, 36, 49])
