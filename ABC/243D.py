n, x = map(int, input().split())
s = list(input())
i = 0
while i < n:
    if s[i] == "U":
        x //= 2
        i += 1
    elif s[i] == "L":
        if i+1 < n:
            if s[i+1] == "U":
                i += 2
            else:
                x *= 2
                i += 1
        else:
            x *= 2
            i += 1
    elif s[i] == "R":
        if i+1 < n:
            if s[i+1] == "U":
                i += 2
            else:
                x = x*2+1
                i += 1
        else:
            x = x * 2 + 1
            i += 1
print(x)