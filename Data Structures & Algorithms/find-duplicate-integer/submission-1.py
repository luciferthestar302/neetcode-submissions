class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #Brute Force approach(USING HASHMAP), time complexity: O(n), space: O(n)
        # count = {}
        # for num in nums:
        #     count[num] = count.get(num,0) +1

        #     if count[num]>1:
        #         return num

        #No space used: O(1), using Linkedlist cycle detection - Floyd's algorithm

        slow = nums[0]
        fast = nums[0]
        #Phase1: Find the meeting point
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow==fast:
                break
        #Phase2: Find the cycle entry point
        slow = nums[0]
        while slow!=fast:
            slow = nums[slow]
            fast = nums[fast]


        return slow #entry point is the answer
        


        
