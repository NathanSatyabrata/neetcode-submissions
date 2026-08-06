class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        setNums = set(nums)
        highestSequence = 0
        for num in setNums:
            if num - 1 not in setNums:
                sequence = [num]
                start = num
                while start + 1 in setNums:
                    sequence.append(start + 1)
                    start += 1

                if len(sequence) > highestSequence:
                    highestSequence = len(sequence)

        return highestSequence
                
        