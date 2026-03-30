class Solution:
    def isValid(self, s: str) -> bool:
        close_to_open = {
            ')':'(',
            '}':'{',
            ']':'[',
        }

        storage = []
        for char in s:
            if char not in close_to_open:
                storage.append(char)
            else:
                if storage and close_to_open[char] == storage[-1]:
                    storage.pop()
                else:
                    return False
        
        return True if not storage else False
                