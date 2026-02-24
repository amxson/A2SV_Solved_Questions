class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle)>len(haystack):
            return -1
        l,r = 0,len(needle)
        for i in range(len(haystack)):
            if haystack[i] == needle[l]:
                x= i
                while x < len(haystack) and l<r and haystack[x]==needle[l]:
                    l+=1
                    x+=1
                print(l,r)
                if l==r:
                    return i
                else:
                    l=0
        return -1

        
        