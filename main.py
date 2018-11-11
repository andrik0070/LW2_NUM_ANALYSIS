from pprint import pprint
import numpy as np

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
degree_of_polynom = 6
x_degrees = []

for i in range(0, len(x)):
    x_degrees.append([x[i]])

for key, value in enumerate(x):
    for i in range(1, (degree_of_polynom * 2)):
        x_degrees[key].append(x_degrees[key][i - 1] * value)

x_degrees_sum = []

for degree in range(1, (degree_of_polynom * 2) + 1):
    degree_sum = 0
    for el in x_degrees:
        degree_sum += el[degree - 1]
    x_degrees_sum.append(degree_sum)

pprint(x_degrees_sum)
x_degrees_sum.insert(0, len(x)+1)

lin_eq = [[0 for i in range(degree_of_polynom + 1)] for j in range(degree_of_polynom + 1)]

for i in range(degree_of_polynom + 1):
    for j in range(degree_of_polynom + 1):
        lin_eq[i][j] = x_degrees_sum[i+j]

pprint(lin_eq)


B = [sum(y)]

for i in range(0, degree_of_polynom):
    b = 0
    for j in range(0, len(x)):
        b += y[j] * x_degrees[j][i]
    B.append(b)

for i in range(degree_of_polynom + 1):
    lin_eq[i].append(B[i])


pprint(gauss(lin_eq))



