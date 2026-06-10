class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        left, right = 0, len(height)-1
        while left<right:
            area = (right-left) * (min(height[left], height[right])) #IMPORTANT: this is the technique to find the area
            res = max(res, area)
            
            if height[left]<height[right]:
                left = left+1

            else:
                right = right-1
            
        return res



        