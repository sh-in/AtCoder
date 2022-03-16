s, t = map(int, input().split())
c = 0
for i in range(s+1):
    for j in range(s+1):
        for k in range(s+1):
            if i+j+k <=s and i*j*k<=t:
                c += 1
            if i+j+k >s or i*j*k>t:
                break
print(c)