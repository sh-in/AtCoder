n, m = map(int, input().split())
b = []
for i in range(n):
    b.append(list(map(int, input().split())))
s = b[0][0]
r = b[0][0] % 7
for i in range(n):
    for j in range(m):
        if s+j+i*7 != b[i][j] or b[i][j]%7 != r+j:
            print("No")
            exit()
print("Yes")n, m = map(int, input().split())
b = []
for i in range(n):
    b.append(list(map(int, input().split())))
x = b[0][0]//7
y = b[0][0]%7
ind = [1, 2, 3, 4, 5, 6, 0]
s = ind.index(y)
for i in range(n):
    for j in range(m):
        if b[i][j] != (x+i)*7+y+j:
            print("No")
            exit()
        if s+j>6:
            print("No")
            exit()
        elif b[i][j]%7 != ind[s+j]:
            print("No")
            exit()
print("Yes")