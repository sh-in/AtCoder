import math
n = int(input())
a = list(map(int, input().split()))
x = int(input())
s = sum(a)
p = math.floor(x/s)
k = p*s
for i in range(n):
    k += a[i]
    if k > x:
        print(p*n+i+1)
        break