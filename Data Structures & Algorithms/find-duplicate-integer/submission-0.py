class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #Brute Force approach(USING HASHMAP), time complexity: O(n), space: O(n)
        count = {}
        for num in nums:
            count[num] = count.get(num,0) +1

            if count[num]>1:
                return num