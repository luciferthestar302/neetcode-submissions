class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
           # def threeSum(nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()  # Step 1: Sort the array to use two pointers
        length = len(nums)
        
        for i in range(length - 2):
            # Optimization: If the current number is greater than 0, 
            # triplets summing to 0 are impossible because the array is sorted.
            if nums[i] > 0:
                break
                
            # Skip duplicate values for the first element to avoid duplicate triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            # Initialize two pointers
            left, right = i + 1, length - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    
                    # Move both pointers past duplicates
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                        
                    # Move pointers to the next new elements
                    left += 1
                    right -= 1
                    
                elif total < 0:
                    left += 1  # Sum is too small, move left pointer right to increase sum
                else:
                    right -= 1 # Sum is too big, move right pointer left to decrease sum
                    
        return res
