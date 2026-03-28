class Solution:
    def decodeString(self, s: str) -> str:
        i = 0
        def dfs():
            nonlocal i
            result = ""
            num = 0
            while i<len(s):
                ch = s[i]
                if ch.isdigit():
                    i+=1
                    num = num*10 + int(ch)
                elif ch == '[':
                    i+=1
                    x = dfs()
                    result+= x*num
                    num = 0
                elif ch==']':
                    i+=1
                    return result
                else:
                    result += ch
                    i+=1
            return result
        return(dfs())
