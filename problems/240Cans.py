n, x = map(int, input().split())
a = []
b = []
for i in range(n):
    at, bt = map(int, input().split())
    a.append(at)
    b.append(bt)
dp = [[False for j in range(x+1)] for i in range(n+1)]
dp[0][0] = True
for i in range(n):
    for j in range(x):
        if dp[i][j]:
            if j + a[i] <= x:
                dp[i+1][j+a[i]] = True
            if j + b[i] <= x:
                dp[i+1][j+b[i]] = True
print("Yes" if dp[n][x] else "No")