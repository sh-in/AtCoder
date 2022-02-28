from collections import defaultdict

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

c = defaultdict(int)
for i in range(n):
    c[a[i]] += 1
for i in range(m):
    if b[i] in c:
        if c[b[i]] == 0:
            print("No")
            exit()
        else:
            c[b[i]] -= 1
    else:
        print("No")
        exit()
print("Yes")