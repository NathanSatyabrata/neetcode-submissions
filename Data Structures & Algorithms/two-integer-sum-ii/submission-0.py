class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}
        for i, val in enumerate(numbers):
            diff = target - val
            if diff in seen:
                return [(seen[diff]) + 1, i + 1]
            seen[val] = i
            
        