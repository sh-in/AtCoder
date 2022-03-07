n = int(input())
c = []
ans = 0
for i in range(n):
    c.append(list(map(int, input().split())))
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            x = c[k][0]
            y = c[k][1]
            if (abs((c[i][0]-x)*(c[j][1]-y)-(c[j][0]-x)*(c[i][1]-y))/2) != 0:
                ans += 1
print(ans)