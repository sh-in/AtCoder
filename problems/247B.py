N = int(input())
s, t = [], []
for i in range(N):
  u, v = input().split()
  s.append(u)
  t.append(v)

for i in range(N):
  output = False
  for S in [s[i], t[i]]:
    f = True
    for j in range(N):
      if i!=j:
        if S==s[j] or S==t[j]:
          f = False
    if f:
      output=True
  if not output:
    print("No")
    exit()
print("Yes")