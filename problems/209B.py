n, x = map(int, input().split())
a = list(map(int, input().split()))
i = 0
while x>0:
    if i%2:
        x -= a[i]-1
    else:
        x -= a[i]
    i += 1
    if i==n and x>=0:
        print("Yes")
        exit()
print("No")