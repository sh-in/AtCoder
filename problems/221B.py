s = list(input())
t = list(input())
p = 0
for i in range(len(s)):
    if s[i] != t[i]:
        tmp = s[i+1]
        s[i+1] = s[i]
        s[i] = tmp
        p = i
        break
for i in range(p, len(s)):
    if s[i] != t[i]:
        print("No")
        exit()
print("Yes")