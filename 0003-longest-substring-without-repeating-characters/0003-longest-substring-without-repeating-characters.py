class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash = [-1] * 128
        left = 0 
        maxx = 0
        for right in range(len(s)):
            c =  s[right]
            if hash[ord(c)] != -1:
                left = max(left,hash[ord(c)] + 1)
            hash[ord(c)] = right
            maxx = max(maxx,right - left + 1)
        return maxx