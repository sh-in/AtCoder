n = list(input())
ns = [int(i) for i in n]
output = [0]
for i in range(3):
  output.append(ns[i])
print("".join(map(str, output)))