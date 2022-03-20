s = []
for i in range(4):
    s.append(input())
p = ["H", "2B", "3B", "HR"]
c = 0
for i in range(4):
    if s[i] in p:
        p.remove(s[i])
        c += 1
if c == 4:
    print("Yes")
else:
    print("No")