n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
p = 0
q = 0
for i in range(n):
    if a[i] == b[i]:
        p += 1
    elif a[i] in b:
        q += 1
print(p)
print(q)