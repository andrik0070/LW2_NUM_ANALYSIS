from pprint import pprint
import matplotlib.pyplot as plt
import numpy as np
import math
import time



def gauss(A):
    n = len(A)

    for i in range(0, n):
        maxEl = abs(A[i][i])
        maxRow = i
        for k in range(i + 1, n):
            if abs(A[k][i]) > maxEl:
                maxEl = abs(A[k][i])
                maxRow = k

        for k in range(i, n + 1):
            tmp = A[maxRow][k]
            A[maxRow][k] = A[i][k]
            A[i][k] = tmp

        for k in range(i + 1, n):
            c = -A[k][i] / A[i][i]
            for j in range(i, n + 1):
                if i == j:
                    A[k][j] = 0
                else:
                    A[k][j] += c * A[i][j]

    x = [0 for i in range(n)]
    for i in range(n - 1, -1, -1):
        x[i] = A[i][n] / A[i][i]
        for k in range(i - 1, -1, -1):
            A[k][n] -= A[k][i] * x[i]
    return x


x = [1, 2, 3, 4, 5, 6, 7, 8]
y = [5.95, 20.95, 51.9, 105, 186, 301, 456.1, 657.1]


def ls_approx(x, y, degree_of_polynom):
    x_degrees = []

    for i in range(0, len(x)):
        x_degrees.append([x[i]])

    for key, value in enumerate(x):
        for i in range(1, (degree_of_polynom * 2)):
            x_degrees[key].append(x_degrees[key][i - 1] * value)

    #pprint(x_degrees)

    x_degrees_sum = []

    for degree in range(0, (degree_of_polynom * 2)):
        # for el in x_degrees:
        #     degree_sum += el[degree - 1]
        pprint(degree)
        x_degrees_sum.append(sum([i[degree] for i in x_degrees]))

    pprint(len(x_degrees_sum))

    x_degrees_sum.insert(0, float(len(x)))

    lin_eq = [[0 for i in range(degree_of_polynom + 1)] for j in range(degree_of_polynom + 1)]

    for i in range(degree_of_polynom + 1):
        for j in range(degree_of_polynom + 1):
            lin_eq[i][j] = x_degrees_sum[i + j]


    #pprint(lin_eq)

    B = [sum(y)]

    for i in range(0, degree_of_polynom):
        b = 0
        for j in range(0, len(x)):
            b += y[j] * x_degrees[j][i]
        B.append(b)

    # for i in range(degree_of_polynom + 1):
    #     lin_eq[i].append(B[i])

    return np.linalg.solve(lin_eq, B)


if __name__ == "__main__":
    # pprint(gauss(lin_eq))

    # x1 = [-2.0]
    # y1 = []
    #
    # x2 = [-3.2, -2.1, 0.4, 0.7, 2, 2.5, 2.777]
    # y2 = [10, -2, 0, -7, 7, 0, 0]
    #

    x1 = [-2.0]
    y1 = []

    summ = -2.0

    for i in range(0, 8):
        summ += 0.5
        x1.append(summ)

    for x in x1:
        y1.append(math.sin(5 * x) * 2.71828183 ** x)

    x1 = [0.0, 1.0, 4.0]
    y1 = [3, 1.0, -2.0]

    # x1 = [-3.2, -2.1, 0.4, 0.7, 2, 2.5, 2.777]
    # y1 = [10, -2, 0, -7, 7, 0, 0]

    # pprint(x1)
    # pprint(y1)

    start_time = time.time()

    coeffs = ls_approx(x1, y1, 2)

    pprint(coeffs)

    # pprint("Execution time:" + str(time.time() - start_time))
    #
    # pprint(coeffs)
    xs = np.linspace(-4, 4, 100)
    ys = np.polynomial.polynomial.polyval(xs, coeffs)

    plt.scatter(x1, y1, edgecolors='blue')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.plot(xs, ys, color='red')
    plt.show()
