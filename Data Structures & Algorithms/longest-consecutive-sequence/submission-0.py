class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0 #initalising longest length

        for n in nums:
            #checking if it has left sequence(this we are doing to get a start of sequence)
            if (n-1)  not in numSet:
                length = 0
                while(n+length) in numSet:
                    length+=1
                longest = max(length, longest)
        return longest
        