n, k = map(int, input().split())
p = []
b = []
for i in range(n):
    b.append(i)
    tmp = 0
    a = list(map(int, input().split()))
    for j in range(3):
        tmp += a[j]
    p.append(tmp)
c = zip(p, b)
c = sorted(c, reverse=True)
p, b = zip(*c)
ans = ["No"] * n
for i in range(n):
    if i+1 <= k:
        ans[b[i]] = "Yes"
    elif p[i] + 300 >= p[k-1]:
        ans[b[i]] = "Yes"
for i in range(n):
    print(ans[i])