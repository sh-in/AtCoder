s = input()
l = 0
r = len(s)-1
while l < r:
    if s[l] == "a" and s[r] == "a":
        l+=1
        r-=1
    elif s[r] == "a":
        r-=1
    elif s[l] == s[r]:
        l+=1
        r-=1
    else:
        break
if l>=r:
    print("Yes")
else:
    print("No")