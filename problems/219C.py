from collections import defaultdict

x = list(input())
n = int(input())
s = []
t = [""]*n
ans = [""]*n
for i in range(n):
    s.append(input())
for i in range(n):
    for j in range(len(s[i])):
        p = x.index(s[i][j])
        t[i] = t[i] + chr(ord("a") + p)
m = defaultdict(int)
for i in range(n):
    m[t[i]] += i
m = sorted(m.items())
for i in range(n):
    print(s[m[i][1]])