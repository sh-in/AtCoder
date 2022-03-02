n, q = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
for i in range(q):
    x = int(input())
    l = 0
    r = n-1
    f = 0
    while l <= r:
        m = (l+r) // 2
        if x > a[m]:
            l = m+1
        elif x == a[m]:
            print(n-m)
            f = 1
            break
        else:
            r = m-1
    if f == 0:
        print(n-l)
