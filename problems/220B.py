k = int(input())
a, b = map(int, input().split())
ao = 0
bo = 0
for i in range(len(str(a))):
    r = a % 10
    a //= 10
    ao += r*(k**i)

for i in range(len(str(b))):
    r = b % 10
    b //= 10
    bo += r*(k**i)
print(ao*bo)