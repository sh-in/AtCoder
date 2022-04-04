n, k, x = map(int, input().split())
a = list(map(int, input().split()))
for i in range(n):
    r = a[i]//x
    if k - r >= 0:
        a[i] -= r*x
        k -= r
    else:
        a[i] -= k*x
        k = 0
    if k <= 0:
        break
if k > 0:
    i = 0
    a.sort(reverse=True)
    while k > 0:
        if i >= n:
            break
        a[i] = 0
        i += 1
        k -= 1
print(sum(a))