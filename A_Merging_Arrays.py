x, y = [int(i) for i in input().split()]
lis_1 = [int(i) for i in input().split()]
lis_2 = [int(i) for i in input().split()]
first = 0
second = 0
ans = []
while first < x and second < y:
  if lis_1[first] < lis_2[second]:
    ans.append(lis_1[first])
    first += 1
  else:
    ans.append(lis_2[second])
    second += 1

ans.extend(lis_1[first:])
ans.extend(lis_2[second:])
print(*ans)
