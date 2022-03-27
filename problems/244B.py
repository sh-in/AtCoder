n = int(input())
t = list(input())
x = 0
y = 0
d = 1
for i in range(n):
    if t[i] == "S":
        if d == 1:
            x += 1
        elif d == 2:
            y -= 1
        elif d == 3:
            x -= 1
        elif d == 4:
            y += 1
    elif t[i] == "R":
        if d == 1:
            d = 2
        elif d == 2:
            d = 3
        elif d == 3:
            d = 4
        elif d == 4:
            d = 1
print(x, y)