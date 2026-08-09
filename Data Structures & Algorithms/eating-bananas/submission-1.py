class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        result = max(piles)

        while left<=right:
            mid = (right+left)//2

            #Very important step below:-
            total_hours = 0
            for pile in piles:
                total_hours+=math.ceil(pile/mid) 
            #above can be written in one line as well:- total_hours = sum(math.ceil(pile / mid) for pile in piles)

            if total_hours<=h:
                result = mid
                right = mid-1
            else:
                left = mid+1
        return result
        