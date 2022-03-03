s = list(input())
if len(s) >= 3:
    sh = s[:3]
    p = [['o', 'x', 'x'], ['x', 'o', 'x'], ['x', 'x', 'o']]
    num = 0
    for i in range(3):
        if sh == p[i]:
            num = i
            break
    pl = len(s) // 3
    r = len(s) % 3
    t = p[num] * pl
    for i in range(r):
        t.append(p[num][i])
    print("Yes" if s == t else "No")
else:
    if "".join(s) in ['o', 'x', 'ox', 'xx', 'xo']:
        print("Yes")
    else:
        print("No")