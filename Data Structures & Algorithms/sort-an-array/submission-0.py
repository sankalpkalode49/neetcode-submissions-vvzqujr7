class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) >1:

            left = nums[:len(nums)//2]
            right = nums[len(nums)//2:]

            self.sortArray(left)
            self.sortArray(right)

            i = 0
            j = 0
            k = 0

            while i < len(left) and j <len(right):
                if left[i] < right[j]:
                    nums[k] = left[i]
                    k += 1
                    i +=1
                else:
                    nums[k] = right[j]
                    k += 1
                    j += 1
            while j < len(right):
                nums[k] = right[j]
                k += 1
                j +=1
            while i < len(left):
                nums[k] =left[i]
                k += 1
                i +=1
    
        return nums 

