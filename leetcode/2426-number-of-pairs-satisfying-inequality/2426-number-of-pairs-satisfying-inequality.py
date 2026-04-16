class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        a = [nums1[i] - nums2[i] for i in range(len(nums1))]
        ans = 0

        def merge(l, r):
            nonlocal ans

            p = 0
            for x in l:
                while p < len(r) and r[p] < x - diff:
                    p += 1
                ans += len(r) - p

            i = j = 0
            res = []

            while i < len(l) and j < len(r):
                if l[i] <= r[j]:
                    res.append(l[i])
                    i += 1
                else:
                    res.append(r[j])
                    j += 1

            while i < len(l):
                res.append(l[i])
                i += 1

            while j < len(r):
                res.append(r[j])
                j += 1

            return res

        def merge_sort(x):
            if len(x) <= 1:
                return x

            m = len(x) // 2
            l = merge_sort(x[:m])
            r = merge_sort(x[m:])

            return merge(l, r)

        merge_sort(a)
        return ans