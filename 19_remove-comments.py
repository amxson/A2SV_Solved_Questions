class Solution:
    def removeComments(self, source: list[str]) -> list[str]:
        result = []
        in_block = False
        new_line = ""
        
        for line in source:
            i = 0
            while i < len(line):
                if in_block:
                    if line[i:i+2] == "*/":
                        in_block = False
                        i += 2
                    else:
                        i += 1
                else:
                    if line[i:i+2] == "/*":
                        in_block = True
                        i += 2
                    elif line[i:i+2] == "//":
                        break
                    else:
                        new_line += line[i]
                        i += 1
            if new_line and not in_block:
                result.append(new_line)
                new_line = ""
            elif not in_block:
                new_line = ""
        
        return result
