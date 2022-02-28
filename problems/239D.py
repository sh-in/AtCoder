# 200以下の素数を求める　エラトステネスの篩
prime = [True]*201
prime[0] = False
prime[1] = False
for p in range(15):
    if prime[p]:
        for i in range(p*p, 201, p):
            prime[i] = False

a, b, c, d = map(int, input().split())
for x in range(a, b+1):
    if all(not prime[x+y] for y in range(c, d+1)):
        print(x, x+1, (not prime[x+1]))
        print("Takahashi")
        exit()
print("Aoki")