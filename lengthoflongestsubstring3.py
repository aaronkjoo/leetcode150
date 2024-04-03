class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # s = "abcabcbb"
        # Output: 3
        # Answer: "abc"
        
        # Create a set which cannot contain duplicate values
        charSet = set()
        # Left pointer
        l = 0 
        # Result
        res = 0
        # Iterate through the input string with right pointer
        for r in range(len(s)):
            while s[r] in charSet:
                # If left pointer char in set, remove it then increment left pointer
                charSet.remove(s[l])
                l += 1
                # Add right pointer char to set
            charSet.add(s[r])
            # Length of sliding window
            res = max(res, r - l + 1)
        return res

solution = Solution()
print(solution.lengthOfLongestSubstring("abcb"))