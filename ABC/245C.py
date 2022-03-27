import math

n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
p = [0]*4
for i in range(n-1):
    c = 0
    x = 1
    y = 1
    if p[0] == 0 and p[2] == 0:
        x = 0
    if p[1] == 0 and p[3] == 0:
        y = 0
    if math.fabs(a[i]-a[i+1])<=k:
        p[0] = 1
        c = 1
    else:
        p[0] = 0
    if math.fabs(a[i]-b[i+1])<=k:
        p[1] = 1
        c = 1
    else:
        p[1] = 0
    if math.fabs(b[i]-a[i+1])<=k:
        p[2] = 1
        c = 1
    else:
        p[2] = 0
    if math.fabs(b[i]-b[i+1])<=k:
        p[3] = 1
        c = 1
    else:
        p[3] = 0
    if c == 0:
        print("No")
        exit()
    if i != 0:
        if x == 0 and p[2] == 0 and p[3] == 0:
            print("No")
            exit()
        if y == 0 and p[0] == 0 and p[1] == 0:
            print("No")
            exit()
        if x == 0:
            p[0] = 0
            p[1] = 0
        if y == 0:
            p[2] = 0
            p[3] = 0
print("Yes")