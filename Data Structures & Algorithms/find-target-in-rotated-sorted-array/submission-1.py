class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while left<=right:
            mid = (left+right)//2
            
            if nums[mid]==target:
                return mid
        #Case1: Left half is sorted:-  
            if nums[mid]>=nums[left]:  
                if target>=nums[left] and nums[mid]>target:
                    right = mid-1
                else:
                    left = mid+1
            else:
            #Case2: Right half is sorted:-
                if target>nums[mid] and nums[right]>=target:
                    left = mid+1
                else:
                    right = mid-1
        return -1

        