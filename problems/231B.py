from collections import defaultdict

n = int(input())
s = defaultdict(int)
max = 0
for i in range(n):
    s[input()] += 1
for i in s:
    if max < s[i]:
        max = s[i]
        name = i
print(name)