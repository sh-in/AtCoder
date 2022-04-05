h, w, x, y = map(int, input().split())
s = []
for i in range(h):
    s.append(list(input()))
c = 0
x -= 1
y -= 1
for i in range(y):
    if s[x][y-i-1] == ".":
        c += 1
    else:
        break
for i in range(y, w):
    if s[x][i] == ".":
        c += 1
    else:
        break
for i in range(x):
    if s[x-i-1][y] == ".":
        c += 1
    else:
        break
for i in range(x+1, h):
    if s[i][y] == ".":
        c += 1
    else:
        break
print(c)