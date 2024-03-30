class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1 #last index
        #back from last position, and see what can reach what
        for i in range(len(nums)-2,-1,-1):
            if nums[i] + i >= goal:
                goal = i #you can reach from this new index
        return True if goal == 0 else False
                