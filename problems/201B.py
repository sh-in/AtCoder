n = int(input())
s = []
t = []
for i in range(n):
    st, tt = input().split()
    s.append(st)
    t.append(int(tt))
fm = 0
fn = 0
sm = 0
sn = 0
for i in range(n):
    if t[i] > fm:
        sm = fm
        fm = t[i]
        sn = fn
        fn = i
    elif t[i] > sm:
        sm = t[i]
        sn = i
print(s[sn])