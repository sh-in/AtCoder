a, b, c, d = map(int, input().split())
red = 0
blue = a
for i in range(1, a+1):
    red += c
    blue += b
    if blue <= red*d:
        print(i)
        exit()
print(-1)