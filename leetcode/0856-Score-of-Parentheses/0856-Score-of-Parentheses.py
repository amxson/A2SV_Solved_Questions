class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        total = 0
        stack = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append('(')
            else:
                stack.pop()
                if s[i-1] == '(':
                    total += 2 ** len(stack)

        return total