n = int(input())
a = list(map(int, input().split()))
a.sort()
ans = n * (n-1) // 2
i = 0
while True:
    f = 1
    if i >= n-1:
        break
    for j in range(i+1, n):
        if a[i] == a[j]:
            f += 1
        else:
            break
    ans -= f * (f-1) // 2
    i += f
print(ans)