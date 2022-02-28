n = int(input())
s = []
for i in range(n):
    l = list(input())
    s.append(l)
c = 0
for i in range(n):
    for j in range(n):
        if s[i][j] == "#":
            for k in range(5):
                if j+k+1 >= n:
                    if c<=2:
                        for l in range(5 - k):
                            if j - l - 1 < 0:
                                c = 0
                                break
                            if s[i][j - l - 1] == ".":
                                c += 1
                                if c >= 3:
                                    c = 0
                                    break
                            if l == 5 - k - 1:
                                print("Yes")
                                exit()
                    c = 0
                    break
                if s[i][j+k+1] == ".":
                    c += 1
                    if c >= 3:
                        c = 0
                        break
                if k == 4:
                    print("Yes")
                    exit()
            for k in range(5):
                if i+k+1 >= n:
                    if c<= 2:
                        for l in range(5 - k):
                            if i - l - 1 < 0:
                                c = 0
                                break
                            if s[i - l - 1][j] == ".":
                                c += 1
                                if c >= 3:
                                    c = 0
                                    break
                            if l == 5 - k - 1:
                                print("Yes")
                                exit()
                    c = 0
                    break
                if s[i+k+1][j] == ".":
                    c += 1
                    if c >= 3:
                        c = 0
                        break
                if k == 4:
                    print("Yes")
                    exit()
            for k in range(5):
                if j+k+1 >= n or i+k+1 >= n:
                    if c <= 2:
                        for l in range(5-k):
                            if i-l-1<0 or j-l-1<0:
                                c=0
                                break
                            if s[i - l - 1][j - l - 1] == ".":
                                c += 1
                                if c >= 3:
                                    c = 0
                                    break
                            if l == 5-k-1:
                                print("Yes")
                                exit()
                    c = 0
                    break
                if s[i+k+1][j+k+1] == ".":
                    c += 1
                    if c >= 3:
                        c = 0
                        break
                if k == 4:
                    print("Yes")
                    exit()
            for k in range(5):
                if j-k-1 < 0 or i+k+1 >= n:
                    if c <= 2:
                        for l in range(5 - k):
                            if i + l + 1 >= n or j + l + 1 >= n:
                                c = 0
                                break
                            if s[i + l + 1][j + l + 1] == ".":
                                c += 1
                                if c >= 3:
                                    c = 0
                                    break
                            if l == 5 - k - 1:
                                print("Yes")
                                exit()
                    c = 0
                    break
                if s[i+k+1][j-k-1] == ".":
                    c += 1
                    if c >= 3:
                        c = 0
                        break
                if k == 4:
                    print("Yes")
                    exit()
print("No")