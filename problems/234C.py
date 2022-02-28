k = int(input())
s = list(format(k, "b"))
ans = []
for i in s:
    if i == "1":
        ans.append("2")
    else:
        ans.append("0")
print("".join([s for s in ans]))