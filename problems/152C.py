n = int(input())
p = list(map(int, input().split()))
min = p[0]
c = 0
for i in range(n):
    if p[i] <= min:
        min = p[i]
        c += 1
print(c)