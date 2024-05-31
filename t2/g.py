x = float(input('x: '))
x0 = x / 2
s_n = x / 2
eps = 10 ** (-13)
n = 2
while abs(x0) > eps:
    x0 *= -1 ** (n + 1) * (2 * n - 1) / (2 * n) * x
    n += 1
    s_n += x0

print(1 + s_n)
print((1 + x) ** 0.5)