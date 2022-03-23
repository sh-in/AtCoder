p = int(input())
m = []
t = 1
for i in range(1, 11):
    t *= i
    m.append(t)
c = 9
counter = 0
while True:
    if p <= 0:
        break
    if p < m[c]:
        c -= 1
    else:
        p -= m[c]
        counter += 1
print(counter)