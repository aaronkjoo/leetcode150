class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # mod k in case it's bigger than the length of array
        k = k % len(nums)

        #reverse entire array
        l, r = 0, len(nums) - 1
        while (l < r):
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1
        #reverse first k elements
        l, r = 0, k - 1
        while (l < r):
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1
        #reverse remaining elements
        l, r = k, len(nums) - 1
        while (l < r):
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1        