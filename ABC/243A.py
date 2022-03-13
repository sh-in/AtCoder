v, a, b, c = map(int, input().split())
f = [a, b, c]
fs = ["F", "M", "T"]
while True:
    for i in range(3):
        v -= f[i]
        if v < 0:
            print(fs[i])
            exit()