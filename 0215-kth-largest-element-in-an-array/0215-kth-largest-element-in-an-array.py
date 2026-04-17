import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        target = len(nums) - k

        def partition(l, r):
            p = random.randint(l, r)
            pivot = nums[p]

            i = l
            j = l
            m = r

            while j <= m:
                if nums[j] < pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                    j += 1
                elif nums[j] > pivot:
                    nums[j], nums[m] = nums[m], nums[j]
                    m -= 1
                else:
                    j += 1

            return i, m

        def quick_select(l, r):
            if l <= r:
                left, right = partition(l, r)

                if target < left:
                    return quick_select(l, left - 1)
                elif target > right:
                    return quick_select(right + 1, r)
                else:
                    return nums[target]

        return quick_select(0, len(nums) - 1)