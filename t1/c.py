a1, a2 = 1, 1
s1 = 1
s2 = 2
k0 = 2
n = int(input())
for x in range(3, n+1):
    a_k = a2 + a1 / (2 ** x)
    k0 *= x
    s2 += k0 / a_k
    a1, a2 = a2, a_k

print(s2)