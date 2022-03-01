s = list(input())
t = list(input())
a = ord(s[0])
b = ord(t[0])
n = (b-a+26) % 26
for i in range(len(s)):
    s[i] = chr((ord(s[i])-ord("a")+n) % 26 + ord("a"))
    if s[i] != t[i]:
        print("No")
        exit()
print("Yes")