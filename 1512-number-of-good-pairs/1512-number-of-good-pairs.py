class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        freq_map = {}

        for num in nums:
            if num in freq_map:
                count += freq_map[num]
            freq_map[num] = freq_map.get(num, 0) + 1

        return count