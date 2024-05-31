x = float(input('х: '))
a1 = x
a_n = (abs(4 * a1 ** 2 - 2 * x)) ** 0.5
i = 2
eps = 10 ** -13
while abs(a_n - a1) > eps:
    a1 = a_n
    a_n = (abs(4 * a1 ** 2 - 2 * x)) ** 0.5

print(a_n)