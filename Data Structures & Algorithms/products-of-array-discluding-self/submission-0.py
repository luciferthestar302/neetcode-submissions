class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        res = [1]* (len(nums)) # //creating an output array
        prefix = 1 #setting default value of prefix for index 0

        for i in range(len(nums)):
            res[i] = prefix
            prefix*=nums[i] #updating the prefix value
        postfix = 1

        for i in range (len(nums) - 1, -1, -1): #starting from the end of the giveninput array and going to start
            res[i] *= postfix
            postfix *= nums[i] #updating the postfix value 
        return res
