class Solution:    
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left <= right:
            k = (left + right) // 2

            valid_hours = self.validHours(piles, k, h)
            if valid_hours is False:
                left = k + 1
            else:
                best_score = k
                right = k - 1

        
        return best_score
                

    def validHours(self, piles, k, h) -> int:
        # Returns -1 for invalid amount of hours.
        # Returns amount of hours for valid k
        total_hours = 0
        for i in range(len(piles)):
            total_hours += -(-piles[i] // k)
        
        if total_hours > h:
            return False
        else:
            return True