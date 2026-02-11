x =  int(input())
for i in range(x):
    n = int(input())
    s = input()
    
    ans = float('inf')
    
    for length in [2,3,4,7]:
        for i in range(n-length+1):
            sub = s[i:i+length]
            if sub.count('a') > sub.count('b') and sub.count('a') > sub.count('c'):
                ans = min(ans, length)
    
    print(ans if ans != float('inf') else -1)






    
    



    