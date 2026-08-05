class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1 for i in range(len(nums))]
        suffix = [1 for i in range(len(nums))]

        for x in range(len(nums)):
            if x - 1 >= 0:
                prefix[x] = nums[x - 1] * prefix[x - 1]

        for j in range(len(nums) - 1, -1, -1):
            if j + 1 <= len(nums) - 1:
                suffix[j] = nums[j + 1] * suffix[j + 1]

        res = []

        for k in range(len(nums)):
            res.append(prefix[k] * suffix[k])

        return res

          
        