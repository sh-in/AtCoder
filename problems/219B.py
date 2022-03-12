s1 = input()
s2 = input()
s3 = input()
t = list(input())
s = []
for i in range(len(t)):
    if t[i] == "1":
        s.append(s1)
    elif t[i] == "2":
        s.append(s2)
    elif t[i] == "3":
        s.append(s3)
print("".join(s))