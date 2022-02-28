n, m = map(int, input().split())
a = []
b = []
for i in range(n):
    at, bt = map(int, input().split())
    a.append(at)
    b.append(bt)
c = zip(a, b)
c = sorted(c)
a, b = zip(*c)
ans = 0
for i in range(n):
    for j in range(b[i]):
        if m <= 0:
            print(ans)
            exit()
        ans += a[i]
        m -= 1
# for文内でansが表示できない桁数があった
print(ans)