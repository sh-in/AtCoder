n = int(input())
a = list(map(int, input().split()))
a.sort()
f = 0
c = 1
for i in range(n):
    for j in range(4):
        if a[4*i + j] != c or i == n-1:
            f = c
            break
    if f != 0:
        break
    c += 1
print(f)