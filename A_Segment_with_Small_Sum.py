x, y = [int(i) for i in input().split()]
lis = [int(i) for i in input().split()]
_max = 0
left, right = 0, 0
_sum = 0
while right < x:
    print(_sum)
    if right == left:
        if lis[left] > y:
            left += 1
            right += 1
    if _sum <= y:
        _max = max(_max, right - left)
    if _sum < y:
        _sum += lis[right]
        right += 1
    else:
        _sum -= lis[left]
        left += 1
print(_max)