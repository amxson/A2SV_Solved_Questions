class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dictt1 = {}
        min = float('inf')
        ans = []
        for i,n in enumerate(list1):
            dictt1[n] = i
        for i,n in enumerate(list2):
            if n in dictt1:
                s = i+dictt1[n]
                if s<min:
                    min = s
                    ans = [n]
                elif s==min:
                    ans.append(n)
        return ans


        