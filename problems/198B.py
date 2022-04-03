n = list(input())
while True:
    if len(n) == 0:
        break
    if n[0] == "0":
        n.remove(n[0])
    else:
        n.reverse()
        break
while True:
    if len(n) == 0:
        break
    if n[0] == "0":
        n.remove(n[0])
    else:
        break
l = 0
if len(n) == 0:
    print("Yes")
    exit()
r = len(n)-1
while True:
    if l >= r:
        print("Yes")
        exit()
    if n[l] == n[r]:
        l += 1
        r -= 1
    else:
        print("No")
        exit()