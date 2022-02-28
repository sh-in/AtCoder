from collections import defaultdict

n, k = map(int, input().split())
c = list(map(int, input().split()))

m = defaultdict(int)
for i in range(k):
    m[c[i]] += 1
ans = len(m)
for i in range(k, n):
    m[c[i]] += 1
    m[c[i-k]] -= 1
    if m[c[i-k]] == 0:
        del m[c[i-k]]
    ans = max(len(m), ans)
print(ans)