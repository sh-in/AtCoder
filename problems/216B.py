n = int(input())
name = []
for i in range(n):
    name.append(input())
for i in range(n):
    for j in range(i+1, n):
        if name[i] == name[j]:
            print("Yes")
            exit()
print("No")