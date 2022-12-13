x = dict()
y = dict()
for i in range(3):
  xin, yin = map(int, input().split())
  if xin in x:
    x[xin] = x[xin] + 1
  else:
    x[xin] = 1
  if yin in y:
    y[yin] = y[yin] + 1
  else:
    y[yin] = 1
xout = [k for k, v in x.items() if v == 1][0]
yout = [k for k, v in y.items() if v == 1][0]
print(xout, yout)