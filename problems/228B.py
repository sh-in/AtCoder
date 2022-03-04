n, x = map(int, input().split())
a = list(map(int, input().split()))
c = 1
k = [False] * (n+1)
k[x] = True
i = a[x-1]
while True:
    if k[i] == False:
        c += 1
        k[i] = True
        i = a[i-1]
    else:
        break
print(c)