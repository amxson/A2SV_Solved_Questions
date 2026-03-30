from collections import Counter

test = int(input())
for _ in range(test):
    n, l, r = map(int, input().split())
    arr = list(map(int, input().split()))
    
    left = Counter(arr[:l])
    right = Counter(arr[l:])
    cost = 0

    
    for color in list(left.keys()):
        x = min(left[color], right.get(color, 0))
        left[color] -= x
        right[color] -= x
        l -= x
        r -= x

    if l < r:
        l, r = r, l
        left, right = right, left

    
    need = (l - r) // 2
    for color in left:
        if need == 0:
            break
        x = min(need, left[color] // 2)
        left[color] -= 2 * x
        l -= 2 * x
        cost += x
        need -= x

    
    cost += need
    l -= need   
    r += need
    
    cost += (l + r) // 2
    print(cost)