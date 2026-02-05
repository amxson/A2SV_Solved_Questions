from collections import Counter
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:

        c = Counter(chars)
        x = 0
        for i in words:
            s = Counter(i)
            if all(s[ch]<=c[ch] for ch in s):
                x += len(i)
        return x



        