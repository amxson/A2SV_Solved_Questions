class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictt = {}
        for i in strs:
            j = "".join(sorted(i))
            dictt[j]=dictt.get(j,[])+[i]
        return list(dictt.values())



        