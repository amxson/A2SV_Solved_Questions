class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mp = {"(":")","{":"}","[":"]"}

        for c in s:

            if c in mp:
                stack.append(c)

            else:
                if not stack:
                    return False

                a = stack.pop()

                if mp[a] != c:
                    return False

        return stack == []

            
        