class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        h = {}
        subStr = ""
        count = 0
        while count < len(pattern) - 1:
            for i in range(len(s)):
                if s[i] != " ":
                    subStr += s[i]
                if s[i] == " " and subStr not in h:
                    c = pattern[count]
                    h[c] = subStr
                    subStr = ""
                    count += 1
                if s[i] == " " and subStr in h:
                    return False
                
        return True


solution = Solution()
print(solution.wordPattern("abba", "dog cat cat mouse"))
