n = int(input())
a = []
b = []
ai = 0
bi = 0
sa = 0
sb = 0
for i in range(n):
    at, bt = map(int, input().split())
    a.append(at)
    b.append(bt)
ans = 10**20
for i in range(n):
    for j in range(n):
        if i==j:
            ans = min(ans, a[i]+b[j])
        else:
            ans = min(ans, max(a[i], b[j]))
print(ans)