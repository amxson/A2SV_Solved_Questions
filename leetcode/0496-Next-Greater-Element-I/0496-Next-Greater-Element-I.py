class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        ans = {}
        for i in range(len(nums2)-1,-1,-1):
            while stack and stack[-1]<=nums2[i]:
                stack.pop()
            if stack:
                ans[nums2[i]] = stack[-1]
            else:
                ans[nums2[i]] = -1
            stack.append(nums2[i])
        for i in range(len(nums1)):
            nums1[i]=ans[nums1[i]]
        return nums1