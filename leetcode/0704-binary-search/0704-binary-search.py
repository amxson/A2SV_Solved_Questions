class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def fun(l, r):
            if l > r:
                return -1
            
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return fun(mid + 1, r)
            else:
                return fun(l, mid - 1)

        return fun(0, len(nums) - 1)