n = int(input())
h = list(map(int, input().split()))
ans = h[0]
for i in range(n):
    if i != n-1:
        if ans < h[i+1]:
            ans = h[i+1]
        else:
            break
print(ans)
