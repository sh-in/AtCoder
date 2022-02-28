n, x = map(int, input().split())
a = []
b = []
d = []
s = 0
l = 0
for i in range(n):
    at, bt = map(int, input().split())
    a.append(at)
    b.append(bt)
    d.append(bt-at)
    s += at
    l += bt
r = x - s
r2 = l - x
if r < 0 or r2 < 0:
    print("No")
elif r in d:
    print("Yes")
else:
    d.sort()
    while True:
        p = 0
        for i in range(len(d)):
            if r > d[i]:
                p = i
            else:
                break
        if p == 0:
            print("No")
            exit()
        else:
            if len(d) != 0:
                r -= d[0]
                del d[0]
                if r in d:
                    print("Yes")
                    exit()
            else:
                print("No")
                exit()
