x = float(input('х: '))
x0 = x
s_n = x
eps = 10 ** (-13)
n = 1
while abs(x0) > eps:
    x0 *= - x**2 * (2 * n - 1) / (n * (2 * n + 1))
    n += 1
    s_n += x0

print(s_n, "n =", n)