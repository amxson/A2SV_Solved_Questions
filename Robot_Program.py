n = int(input())
for _ in range(n):
    nc, x, s = map(int, input().split())
    c = input()
    
    pos = x
    first_hit = -1
    
    for i in range(nc):
        if c[i] == 'L':
            pos -= 1
        else:
            pos += 1
            
        if pos == 0:
            first_hit = i + 1
            break
    

    if first_hit == -1:
        print(0)
        continue

    if first_hit > s:
        print(0)
        continue
    
    
    answer = 1
    remaining = s - first_hit
    
    
    pos = 0
    cycle_len = -1
    
    for i in range(nc):
        if c[i] == 'L':
            pos -= 1
        else:
            pos += 1
            
        if pos == 0:
            cycle_len = i + 1
            break
    
    if cycle_len == -1:
        print(answer)
    else:
        answer += remaining // cycle_len
        print(answer)
