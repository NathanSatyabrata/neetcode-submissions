class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        setNums = set(nums)
        highestSequence = 0
        for num in setNums:
            if num - 1 not in setNums:
                length = 0
                while num + length in setNums:
                    length += 1

                highestSequence = max(highestSequence, length)

        return highestSequence
                
        