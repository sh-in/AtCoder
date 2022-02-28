import math

n, d = map(int, input().split())
a = []
for i in range(n):
    x = list(map(int, input().split()))
    a.append(x)
c = 0
for i in range(n-1):
    for k in range(i+1, n):
        ans = 0
        for j in range(d):
            ans += (a[i][j] - a[k][j]) ** 2
        ans = math.sqrt(ans)
        if ans.is_integer():
            c += 1
print(c)