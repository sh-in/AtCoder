l, r = map(int, input().split())
s = list(input())
a = s[:l-1]
b = s[l-1:r]
c = s[r:]
b.reverse()
print("".join([i for i in (a+b+c)]))