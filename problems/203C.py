n, k = map(int, input().split())
a = []
b = []
for i in range(n):
    x, y = map(int, input().split())
    a.append(x)
    b.append(y)

c = zip(a, b)
c = sorted(c)
a, b = zip(*c)

for i in range(n):
    if k < a[i]:
        break
    else:
        k += b[i]

print(k)

# 下のコードはTLEになった
# p = 0
# while k > 0:
#     k -= 1
#     p += 1
#     while True:
#         if p in a:
#             pp = a.index(p)
#             k += b[pp]
#             del a[pp]
#             del b[pp]
#         else:
#             break
# print(p)