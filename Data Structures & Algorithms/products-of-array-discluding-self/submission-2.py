class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1 for i in range(len(nums))]
        suffix = [1 for i in range(len(nums))]

        output = [1 for i in range(len(nums))]

        prefix = 1
        for x in range(len(nums)):
            output[x] = prefix
            prefix *= nums[x]

        suffix = 1
        for j in range(len(nums) - 1, -1, -1):
            output[j] *= suffix
            suffix *= nums[j]

        return output

          
        