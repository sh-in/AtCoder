a, b, c, d = map(int, input().split())
if a < c:
    print("Takahashi")
elif c < a:
    print("Aoki")
elif b < d:
    print("Takahashi")
elif d < b:
    print("Aoki")
else:
    print("Takahashi")