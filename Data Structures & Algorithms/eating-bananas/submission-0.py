class Solution:    
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        best_score = float('inf')
        flag = False

        while left <= right and not flag:
            k = (left + right) // 2

            total_hours = self.totalHours(piles, k, h)
            if total_hours == -1:
                left = k + 1
            elif k < best_score:
                best_score = k
                right = k - 1
            else:
                flag = True
        
        return best_score
                

    def totalHours(self, piles, k, h) -> int:
        # Returns -1 for invalid amount of hours.
        # Returns amount of hours for valid k
        total_hours = 0
        for i in range(len(piles)):
            total_hours += -(-piles[i] // k)
        
        if total_hours > h:
            return -1
        else:
            return total_hours