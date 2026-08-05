class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        newlist = []
        for i in range(len(nums)):
            product = 1
            for j in range(len(nums)):
                if i != j:
                    product *= nums[j]

                if j == len(nums) - 1:
                    newlist.append(product)

        return newlist
        