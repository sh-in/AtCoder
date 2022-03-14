c = ["ABC", "ARC", "AGC", "AHC"]
s = []
for i in range(3):
    s.append(input())
for i in range(4):
    if c[i] not in s:
        print(c[i])