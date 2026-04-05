class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0  # Index to place elements not equal to val
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]  # Place non-val element at index k
                k += 1  # Increment count of valid elements
        return k