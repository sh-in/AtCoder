n = int(input())
a = []
ans = False
for i in range(n):
    a.append(input())
for i in range(n):
    for j in range(n):
        if i+5 < n:
            c = 0
            for k in range(6):
                if a[i+k][j] == "#":
                    c += 1
                if c >= 4:
                    ans = True
        if j+5 < n:
            c = 0
            for k in range(6):
                if a[i][j+k] == "#":
                    c += 1
                if c >= 4:
                    ans = True
        if i+5 < n and j+5 < n:
            c = 0
            for k in range(6):
                if a[i+k][j+k] =="#":
                    c += 1
                if c >= 4:
                    ans = True
        if i+5 < n and j-5 >= 0:
            c = 0
            for k in range(6):
                if a[i+k][j-k] == "#":
                    c += 1
                if c >= 4:
                    ans = True
print("Yes" if ans else "No")