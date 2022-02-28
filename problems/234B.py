import math

n = int(input())
a = []
max = 0
for i in range(n):
    a.append(list(map(int, input().split())))
for i in range(n):
    for j in range(i+1, n):
        tmp = math.sqrt((a[i][0] - a[j][0]) ** 2 + (a[i][1] - a[j][1]) ** 2)
        if tmp > max:
            max = tmp
print(max)