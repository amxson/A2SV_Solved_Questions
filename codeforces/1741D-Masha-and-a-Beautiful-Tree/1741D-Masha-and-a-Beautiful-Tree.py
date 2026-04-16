def merge(l, r):
        if max(l) < min(r):
            return l + r
        elif max(r) < min(l):
            c[0] += 1
            return r + l
        else:
            return -1

    def merge_sort(a):
        if len(a) <= 1:
            return a

        md = len(a) // 2
        l = merge_sort(a[:md])
        if l == -1:
            return -1
        r = merge_sort(a[md:])
        if r == -1:
            return -1

        return merge(l, r)

    ans = merge_sort(nums)
    if ans == -1:
        print(-1)
    else:
        print(c[0])