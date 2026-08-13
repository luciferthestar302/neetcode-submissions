class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums_merged = sorted(nums1+nums2)
        A = len(nums1)+len(nums2)
        left, right = 0, A-1
        mid = (left+right)//2
        if A%2!=0:
            median = nums_merged[mid] #if it's odd
        else:
            median = (nums_merged[mid]+nums_merged[mid+1])/2 #if it's even
        return median