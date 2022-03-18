from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))
m = defaultdict(list)

for i in range(n):
    m[i+1].append(a[i])
m = sorted(m.items(), key=lambda x:x[1])
print(m[-2][0])