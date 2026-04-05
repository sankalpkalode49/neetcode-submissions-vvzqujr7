class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 1
        while i <=  n:
            nums1.pop(-i)
            nums1.append(nums2[i-1])
            i +=1
        
        nums1.sort()
        
        