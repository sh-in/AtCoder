h, w = map(int, input().split())
a = []
for i in range(h):
    a.append(list(map(int, input().split())))
for i in range(h-1):
    for j in range(w-1):
        for p in range(i+1, h):
            for q in range(j+1, w):
                if a[i][j] + a[p][q] > a[p][j] + a[i][q]:
                    print("No")
                    exit()
print("Yes")