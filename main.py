from tabulate import tabulate
import math
import numpy as np


def solve(a, b, c, d):
    if (a == 0 and b == 0):
        return np.array([(-d * 1.0) / c])

    elif (a == 0):

        D = c * c - 4.0 * b * d
        if D >= 0:
            D = math.sqrt(D)
            x1 = (-c + D) / (2.0 * b)
            x2 = (-c - D) / (2.0 * b)
        else:
            D = math.sqrt(-D)
            x1 = (-c + D * 1j) / (2.0 * b)
            x2 = (-c - D * 1j) / (2.0 * b)

        return np.array([x1, x2])

    f = findF(a, b, c)
    g = findG(a, b, c, d)
    h = findH(g, f)

    if f == 0 and g == 0 and h == 0:
        if (d / a) >= 0:
            x = (d / (1.0 * a)) ** (1 / 3.0) * -1
        else:
            x = (-d / (1.0 * a)) ** (1 / 3.0)
        return np.array([x, x, x])

    elif h <= 0:

        i = math.sqrt(((g ** 2.0) / 4.0) - h)
        j = i ** (1 / 3.0)
        k = math.acos(-(g / (2 * i)))
        L = j * -1
        M = math.cos(k / 3.0)
        N = math.sqrt(3) * math.sin(k / 3.0)
        P = (b / (3.0 * a)) * -1

        x1 = 2 * j * math.cos(k / 3.0) - (b / (3.0 * a))
        x2 = L * (M + N) + P
        x3 = L * (M - N) + P

        return np.array([x1, x2, x3])
    elif h > 0:
        R = -(g / 2.0) + math.sqrt(h)
        if R >= 0:
            S = R ** (1 / 3.0)
        else:
            S = (-R) ** (1 / 3.0) * -1
        T = -(g / 2.0) - math.sqrt(h)
        if T >= 0:
            U = (T ** (1 / 3.0))
        else:
            U = ((-T) ** (1 / 3.0)) * -1

        x1 = (S + U) - (b / (3.0 * a))
        x2 = -(S + U) / 2 - (b / (3.0 * a)) + (S - U) * math.sqrt(3) * 0.5j
        x3 = -(S + U) / 2 - (b / (3.0 * a)) - (S - U) * math.sqrt(3) * 0.5j

        return np.array([x1, x2, x3])
def findF(a, b, c):
    return ((3.0 * c / a) - ((b ** 2.0) / (a ** 2.0))) / 3.0

def findG(a, b, c, d):
    return (((2.0 * (b ** 3.0)) / (a ** 3.0)) - ((9.0 * b * c) / (a ** 2.0)) + (27.0 * d / a)) / 27.0

def findH(g, f):
    return ((g ** 2.0) / 4.0 + (f ** 3.0) / 27.0)

def nums(num):
    if num < 10:
        if num == 1:
            return "₁"
        elif num == 2:
            return "₂"
        elif num == 3:
            return "₃"
        elif num == 4:
            return "₄"
        elif num == 5:
            return "₅"
        elif num == 6:
            return "₆"
        elif num == 7:
            return "₇"
        elif num == 8:
            return "₈"
        elif num == 9:
            return "₉"
    else:
        return "n"

def myround(num):
    return round(num, 3)


e = 0.001
A = [2, 9, 0, -4]
a_b = [0, 1]


def fun(x):
    sum = 0
    g = 3
    for i in range(len(A)):
        sum += A[i] * (x**g)
        g -= 1
    return sum

data = []
count = 0
while abs(a_b[1] - a_b[0]) > e:
    b = []
    c = (a_b[0] + a_b[1]) / 2
    b.extend([count, myround(fun(a_b[0])), myround(a_b[0]), myround(a_b[1]), myround(fun(a_b[1])), myround(c), myround(fun(c)), (a_b[1] - a_b[0])])
    if fun(a_b[0]) * fun(c) < 0:
        a_b[1] = c
    else:
        a_b[0] = c
    count += 1
    data.append(b)
b = []
b.extend([count, myround(fun(a_b[0])), myround(a_b[0]), myround(a_b[1]), myround(fun(a_b[1])), myround(c), myround(fun(c)), (a_b[1] - a_b[0])])
data.append(b)

print (tabulate(data, headers=["k", "f(a)", "a", "b", "f(b)", "c", "f(c)", "|b - a|"]))

X = solve(*A)
print()
for i in range(len(X)):
    print(f"X{nums(i+1)} = {myround(X[i])}")