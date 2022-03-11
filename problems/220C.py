import math
n = int(input())
a = list(map(int, input().split()))
x = int(input())
s = sum(a)
p = math.floor(x/s)
k = p*s
f = 0
for i in range(n):
    if k > x:
        f = 1
        print(p*n+i)
        break
    else:
        k += a[i]
if f == 0 and k > x:
    print(p*n+n)