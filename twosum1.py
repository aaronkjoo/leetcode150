class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        checkMap = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in checkMap:
                return [checkMap[diff], i]
            checkMap[n] = i