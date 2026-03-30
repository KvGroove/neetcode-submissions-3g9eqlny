class Solution:
    def isValid(self, s: str) -> bool:
        close_to_open = {
            ')':'(',
            ']':'[',
            '}':'{',
        }

        close_to_open[')']

        stack = []
        for char in s:
            if char in close_to_open:
                if not stack:
                    stack.append('.')
                    break
                elif close_to_open[char] != stack.pop():
                    stack.append('.')
                    break
            else:
                stack.append(char)
        
        return not stack