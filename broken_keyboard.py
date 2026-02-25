tests = int(input())    
for _ in range(tests):
    s = input().strip()
    arr = list(s)
    l= 0
  
    ans = []
    while l < len(arr):
        h = l
        while h < len(arr) and arr[h] == arr[l]:
            h += 1
        if (h-l) % 2 == 1:
            ans.append(arr[l])
        l = h
    print("".join(sorted(set(ans))))

            
                

        
        
            
            


