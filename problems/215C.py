import itertools

s, k = input().split()
s = list(s)
s.sort()
k = int(k)
sl = sorted(set(list(itertools.permutations(s))))
print("".join(sl[k-1]))