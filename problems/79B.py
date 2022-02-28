n = int(input())
l0 = 2
l1 = 1
for i in range(n-1):
    tmp = l0 + l1
    l0 = l1
    l1 = tmp
print(l1)