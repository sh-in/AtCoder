from fractions import Fraction

n = int(input())
a = []
b = []
t = 0.0
tl = []
for i in range(n):
    at, bt = map(int, input().split())
    a.append(at)
    b.append(bt)
    t += Fraction(at/bt)
    tl.append(Fraction(at/bt))
ht = Fraction(t/2.0)
ans = 0.0
ct = 0
i = 0
while True:
    if ct + tl[i] > ht:
        ans += (ht-ct)*b[i]
        break
    ans += a[i]
    ct += tl[i]
    i += 1
print(ans)