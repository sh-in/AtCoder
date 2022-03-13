n = int(input())
c = []
for i in range(n):
    c.append(list(map(int, input().split())))
s = list(input())
r = []
l = []
for i in range(n):
    if s[i] == "R":
        r.append(c[i])
    else:
        l.append(c[i])
r.sort(key=lambda x:x[1])
l.sort(key=lambda x:x[1])
np = 0
pp = 0
if len(r) < len(l):
    for i in range(len(r)):
        x = r[i][0]
        y = r[i][1]
        if i != 0:
            if y == r[i-1][1]:
                for j in range(pp, len(l)):
                    if y == l[j][1] and x < l[j][0]:
                        print("Yes")
                        exit()
                    elif y < l[j][1]:
                        np = j
                        break
            else:
                pp = np
                for j in range(pp, len(l)):
                    if y == l[j][1] and x < l[j][0]:
                        print("Yes")
                        exit()
                    elif y < l[j][1]:
                        np = j
                        break
        else:
            for j in range(len(l)):
                if y == l[j][1] and x < l[j][0]:
                    print("Yes")
                    exit()
                elif y < l[j][1]:
                    np = j
                    break
else:
    for i in range(len(l)):
        x = l[i][0]
        y = l[i][1]
        if i != 0:
            if y == l[i-1][1]:
                for j in range(pp, len(r)):
                    if y == r[j][1] and x > r[j][0]:
                        print("Yes")
                        exit()
                    elif y < r[j][1]:
                        np = j
                        break
            else:
                pp = np
                for j in range(pp, len(r)):
                    if y == r[j][1] and x > r[j][0]:
                        print("Yes")
                        exit()
                    elif y < r[j][1]:
                        np = j
                        break
        else:
            for j in range(len(r)):
                if y == r[j][1] and x > r[j][0]:
                    print("Yes")
                    exit()
                elif y < r[j][1]:
                    np = j
                    break
print("No")