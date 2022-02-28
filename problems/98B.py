n = int(input())
s = list(input())
max = 0
for i in range(1, n):
    a = s[:i]
    b = s[i:]
    c = 0
    for j in range(97, 123):
        if chr(j) in a and chr(j) in b:
            c += 1
    if c > max:
        max = c
print(max)