class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r = 0, len(height) - 1
        maxArea = 0 

        while l < r:
            width = r - l
            h = min(height[l], height[r])
            area = width * h
            maxArea = max(area, maxArea)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return maxArea
        