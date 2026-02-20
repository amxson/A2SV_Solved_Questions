tests = int(input())
for _ in range(tests):
    n, k = map(int, input().split())
    arr = [list(map(int, input().split())) for __ in range(n)]

    arr.sort()  
    maxx = k
    i = 0

    while i < n:
        changed = False
        
        while i < n and arr[i][0] <= maxx:
            maxx = max(maxx, arr[i][2])
            i += 1
            changed = True
        
        if not changed:
            break

    print(maxx)