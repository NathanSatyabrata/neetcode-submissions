class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        setNums = set(nums)
        highestSequence = 0
        for num in setNums:
            if num - 1 not in setNums:
                length = 1
                start = num
                while start + 1 in setNums:
                    length += 1
                    start += 1

                highestSequence = max(highestSequence, length)

        return highestSequence
                
        