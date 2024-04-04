class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sMap, tMap = {}, {}
        if len(t) != len(s):
            return False
        for i in range(len(s)):
            sMap[s[i]] = 1 + sMap.get(s[i], 0)
            tMap[t[i]] = 1 + tMap.get(t[i], 0)
        for c in sMap:
            if sMap[c] != tMap.get(c, 0):
                return False
        return True
        

        