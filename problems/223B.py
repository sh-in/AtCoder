s = input()
min = str(s)
max = str(s)
for i in range(len(s)-1):
    s = s + s[0]
    s = s[1:]
    if s<min:
        min=s
    if s>max:
        max=s
print(min)
print(max)