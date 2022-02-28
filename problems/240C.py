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
            if a[i] + j <= x:
                dp[i+1][a[i]+j] = True
            if b[i] + j <= x:
                dp[i+1][b[i]+j] = True
print("Yes" if dp[n][x] else "No")