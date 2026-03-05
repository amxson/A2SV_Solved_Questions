t = int(input())
for _ in range(t):
    r = int(input())
    rr = list(map(int,input().split()))
    b = int(input())
    bb= list(map(int,input().split()))
    cr = 0
    maxr = 0
    for i in range(r):
        cr+=rr[i]
        maxr = max(maxr,cr)
    cb = 0
    maxb = 0
    for i in range(b):
        cb+=bb[i]
        maxb = max(maxb,cb)
    print(maxr+maxb)