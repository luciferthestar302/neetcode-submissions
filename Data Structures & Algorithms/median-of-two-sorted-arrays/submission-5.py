class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #NOTE: We are doing binary search on smaller array, hence making sure the nums1 is smaller
        if len(nums1)>len(nums2):
            nums1, nums2= nums2, nums1

        m, n = len(nums1), len(nums2)
        left, right = 0, m
        while left<=right:
            x = (left+right)//2
            y = (m+n)//2 - x

            L1 = nums1[x-1] if x>0 else float('-inf')
            R1 = nums1[x]   if x < m else float('inf')
            L2 = nums2[y-1] if y > 0 else float('-inf')
            R2 = nums2[y]   if y < n else float('inf')

            if L1 <= R2 and L2 <= R1:      # valid partition!
                if (m + n) % 2 == 1:
                    return min(R1, R2)
                else:
                    return (max(L1, L2) + min(R1, R2)) / 2
            elif L1 > R2:
                right = x - 1             # x too large
            else:
                left = x + 1 
        
        



        # #The below code is written by my own which is actually wrong, because time complexity here is O((m+n)log(m+n)), question has asked time complexity o(log(m+n)):-
        # nums_merged = sorted(nums1+nums2)
        # A = len(nums1)+len(nums2)
        # left, right = 0, A-1
        # mid = (left+right)//2
        # if A%2!=0:
        #     median = nums_merged[mid] #if it's odd
        # else:
        #     median = (nums_merged[mid]+nums_merged[mid+1])/2 #if it's even
        # return median