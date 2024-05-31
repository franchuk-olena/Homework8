a1, a2 = 0, 1
b1, b2 = 1, 1
s1 = 2
s2 = 4
n = int(input())
for x in range(3, n+1):
    b_k = b2 + a2
    a_k = a2 / x + a1 * b_k
    s2 += (2 ** x / (a_k + b_k))
    b1, b2 = b2, b_k
    a1, a2 = a2, a_k

print(s2)