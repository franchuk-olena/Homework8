a1, a2 = 1, 1
s1 = 3
s2 = 12
n = int(input())
for x in range(3, n+1):
    a_k = a2 / x + a1
    s2 += 3 ** x / a_k
    a1, a2 = a2, a_k

print(s2)