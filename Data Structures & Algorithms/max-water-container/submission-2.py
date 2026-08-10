class Solution:
    def maxArea(self, heights: List[int]) -> int:

        highest = 0
        l, r = 0, len(heights) - 1
        while l < r:
            distance = r - l
            height = min(heights[l], heights[r])
            water = distance * height

            if water > highest:
                highest = water
            if l < r and height == heights[l]:
                l += 1
            elif l < r and height == heights[r]:
                r -= 1
            
            
        
        return highest


        