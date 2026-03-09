class Solution:
    def simplifyPath(self, path: str) -> str:
        s = path.split("/")
        z =  []
        for x in s:
            if x == '' or x== '.':
                continue
            elif  x == '..' :
                if z:
                 z.pop()
            else:    
                z.append(x)
    
        return '/' +'/'.join(z)

        