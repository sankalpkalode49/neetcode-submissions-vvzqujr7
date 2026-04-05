class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count frequency of each element
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        # Step 2: Create buckets where index = frequency
        n = len(nums)
        bucket = [[] for _ in range(n + 1)]  # Max frequency can be n
        for num, count in freq.items():
            bucket[count].append(num)
        
        # Step 3: Collect top k frequent elements
        result = []
        for i in range(n, -1, -1):  # Iterate from highest to lowest frequency
            if bucket[i]:  # If bucket is not empty
                result.extend(bucket[i])  # Add all elements in this bucket
                if len(result) >= k:  # Stop once we have k elements
                    return result[:k]
        
        return result[:k]  # Return first k elements (in case of edge cases)