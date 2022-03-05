n = int(input())
a = []
for i in range(n-1):
    a.append(list(map(int, input().split())))
if a[0][0] in a[1]:
    c = a[0][0]
elif a[0][1] in a[1]:
    c = a[0][1]
else:
    print("No")
    exit()
for i in range(2, n-1):
    if c not in a[i]:
        print("No")
        exit()
print("Yes")