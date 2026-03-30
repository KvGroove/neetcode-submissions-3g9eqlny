class Solution:
    # Invariants
    # 1) At any point of the loop, the stack will contain
    #    unmatched opening brackets in the correct order
    # 2) When a closing bracket appears, the top of the bracket
    #    must be its matching opening bracket

    def isValid(self, s:str) -> bool:
        close_to_open = {
            ')':'(',
            '}':'{',
            ']':'[',
        }
    
        stack = []
        # Typo
        for char in s:
            if char in close_to_open:
                # Must be the mapped character
                if stack and close_to_open[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        
        return True if not stack else False