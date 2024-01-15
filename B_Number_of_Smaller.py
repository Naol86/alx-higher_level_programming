x, y = [int(i) for i in input().split()]
lis_1 = [int(i) for i in input().split()]
lis_2 = [int(i) for i in input().split()]
ans = []
upper = 0
lower = 0
while (upper < x) and (lower < y):
  if lis_2[lower] > lis_1[upper]:
    upper += 1
    continue
  ans.append(upper)
  lower += 1


leng = len(ans)
while leng < y:
  ans.append(upper)
  leng += 1
print(*ans)