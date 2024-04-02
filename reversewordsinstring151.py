class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        arr = s.split()

        res = ""
        for i in range(len(arr)-1,-1,-1):
            res += arr[i]
            if i > 0:
                res += " "
        return res
        