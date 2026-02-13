from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        c = Counter(word1)
        c2 = Counter(word2)
        x1 = list(c.values())
        x2 = list(c2.values())
        if sorted(x1)==sorted(x2):
            for i in word1:
                if i not in word2:
                    return False
            return True
        return False

        


        