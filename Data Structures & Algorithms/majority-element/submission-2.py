class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums = sorted(nums)
        e = len(nums)//2
        element = nums[e]
        return element        