n = int(input())
a = list(map(int, input().split()))
a.sort()
s = set(a)
c = 0
for i in s:
    if c != i:
        print(c)
        exit()
    else:
        c += 1
print(c)