s = input()
n = [int(i) for i in s]
if n.count(n[0]) == 4:
    print("Weak")
    exit()
c = 0
for i in range(1, 4):
    if n[i-1] == 9:
        if n[i] == 0:
            c += 1
    elif n[i] == n[i-1] + 1:
        c += 1
if c == 3:
    print("Weak")
else:
    print("Strong")