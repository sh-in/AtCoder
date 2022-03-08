n, p = map(int, input().split())
a = list(map(int, input().split()))
c = 0
for i in range(n):
    if a[i] < p:
        c += 1
print(c)