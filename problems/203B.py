n, k = map(int, input().split())
c = 0
for i in range(n):
    for j in range(k):
        c += 100 * (i + 1) + j + 1
print(c)