n = int(input())
s = list(map(int, input().split()))
c = 0
for i in range(n):
    f = 0
    for a in range(1, 1001):
        for b in range(1, 1001):
            if 4*a*b + 3*a + 3*b == s[i]:
                f = 1
                break
            if 4*1*b + 3*a + 3*b >1000:
                break
        if f == 1:
            break
    if f != 1:
        c += 1
print(c)