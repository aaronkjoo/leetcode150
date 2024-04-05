class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:

        if not nums:
            return []
        res = []
        
        start, end = nums[0], nums[0]
        for i in range(1, len(nums)): #iterate through sorted nums input array. 
            #if nums[i] > end + 1:     #and if next nums[i] is start of new range, update your result arry
            if nums[i] - nums[i - 1] > 1:
                if start != end:
                    res.append(str(start) + "->" + str(end))

                else:
                    res.append(str(end))

                start, end = nums[i], nums[i]   #update your start and end values (reset them to be both equal to nums[i])
            else:
                end = nums[i]         # otherwise, your end updates to be the current nums[i] value
        if start != end:
            res.append(str(start) + "->" + str(end))
        else:
            res.append(str(end))
        return res
        
    
    
solution = Solution()
print(solution.summaryRanges([0,1,2,4,5,7]))
"""
Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"
"""