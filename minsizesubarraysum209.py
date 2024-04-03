class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        # [2, 3, 1, 2, 4, 3]
        # target = 7 
        # output = 2
        l, total = 0, 0
        res = float("inf")

        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                res = min(res, r - l + 1)
                total -= nums[l]
                l += 1

        if res == float("inf"):
            return 0
        else:
            return res