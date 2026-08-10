class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        sums = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            l, r = i + 1, len(nums) - 1

            while l < r:
                
                summation = nums[l] + nums[r] + nums[i]
                if summation > 0:
                    r -=1
                elif summation < 0:
                    l += 1
                else:
                    sums.append(tuple([nums[i], nums[l], nums[r]]))
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1

                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1

                    l += 1
                    r -= 1

        return sums