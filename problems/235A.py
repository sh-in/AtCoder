a = list(input())
a = [int(i) for i in a]
ans = 0
for i in a:
    ans += (100*i + 10*i + i)
print(ans)