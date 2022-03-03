a, b = input().split()
l = max(len(a), len(b))
for i in range(l):
    if len(a) < i+1 <= len(b):
        ai = 0
        bi = int(b[len(b) - i - 1])
    elif len(b) < i+1 <= len(a):
        ai = int(a[len(a) - i - 1])
        bi = 0
    else:
        ai = int(a[len(a) - i - 1])
        bi = int(b[len(b) - i - 1])
    if ai + bi >= 10:
        print("Hard")
        exit()
print("Easy")