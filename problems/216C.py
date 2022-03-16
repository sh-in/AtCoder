n = int(input())
s = []
b = 1
while n:
    if n%2:
        n -= 1
        s.append("A")
    else:
        n //= 2
        s.append("B")
s.reverse()
print("".join(s))