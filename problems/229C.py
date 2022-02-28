n, w = map(int, input().split())
a = []
b = []
for i in range(n):
    at, bt = map(int, input().split())
    a.append(at)
    b.append(bt)
c = zip(a, b)
c = sorted(c, reverse=True)
a, b = zip(*c)
i = 0
c = 0
for j in range(n):
    r = b[i]
    while True:
        if w == 0:
            break
        elif r > 0:
            c += a[i]
            w -= 1
            r -= 1
        else:
            i += 1
            break
print(c)