n = int(input())
p = [2, 3, 3, 3, 3, 3, 3, 3, 2]
c = [2, 3, 3, 3, 3, 3, 3, 3, 2]
for i in range(n-2):
    c[0] = (p[0] + p[1])
    c[8] = c[0]
    for j in range(1, 8):
        c[j] = (p[j-1] + p[j] + p[j+1])
    if c[0] > 998244353:
        for j in range(9):
            c[j] %= 998244353
    p = list(c)
print(sum(c) % 998244353)