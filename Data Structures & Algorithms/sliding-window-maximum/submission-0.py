class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left = 0
        res = []
        dq = deque()
        # NOTE: Deque is used to store the index, not the values of nums
        for right in range(len(nums)):
            #R-1 checking if deque is empty and removing smaller element from back in queue
            while dq and nums[dq[-1]]<nums[right]:
                dq.pop() 
            #Adding current index from back in deque
            dq.append(right)
            #R-2 Removing expired index from front
            if dq[0] <left:
                dq.popleft()
            #Storing the maximum to res once window is full
            if right >=k-1:
                res.append(nums[dq[0]]) 
                left+=1
        return res

        