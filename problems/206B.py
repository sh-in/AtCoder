n = int(input())
c = 0
i = 0
while True:
    if c >= n:
        print(i)
        exit()
    else:
        i += 1
        c += i
