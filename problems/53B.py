s = list(input())
a = 0
z = 0
for i in range(len(s)):
    if s[i] == "A":
        a = i
        break
s.reverse()
for i in range(len(s)):
    if s[i] == "Z":
        z = len(s) - i -1
        break
print(z-a+1)