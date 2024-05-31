from math import log, e

x = float(input('х: '))
x1 = x
s_n = x
eps = 10 ** (-13)
n = 2
while abs(x1) > eps:
    x1 *= x ** 2 * (2 * n - 3) / (2 * n - 1)
    n += 1
    s_n += x1

print(2 * s_n)
print(log((1 + x) / (1 - x), e))