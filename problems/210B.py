n = int(input())
t = list(input())
s = [int(i) for i in t]
for i in range(n):
    if s[i] and i%2 == 0:
        print("Takahashi")
        exit()
    elif s[i] and i%2 == 1:
        print("Aoki")
        exit()