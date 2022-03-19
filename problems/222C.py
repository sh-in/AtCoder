n, m = map(int, input().split())
a = [list(input()) for i in range(2 * n)]
p = [[0, i] for i in range(2 * n)]


def jan(h1, h2):
    if h1 == h2: return -1
    if h1 == "G" and h2 == "P": return 1
    if h1 == "C" and h2 == "G": return 1
    if h1 == "P" and h2 == "C": return 1
    return 0


for i in range(m):
    for j in range(n):
        p1 = p[2*j][1]
        p2 = p[2*j+1][1]
        r = jan(a[p1][i], a[p2][i])
        if r != -1:
            p[2*j+r][0] -= 1
    p.sort()

for _,i in p: print(i+1)
