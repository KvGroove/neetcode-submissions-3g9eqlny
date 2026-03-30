class Solution:
    def isValid(self, s: str) -> bool:
        # Map close parentheses to open
        close_to_open = {
            '}':'{',
            ']':'[',
            ')':'(',
        }
        stack = []

        # Main Logic
        for char in s:
            if char in close_to_open:
                if stack and close_to_open[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return True if not stack else False


