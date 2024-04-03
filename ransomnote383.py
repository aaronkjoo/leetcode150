class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        res = {}

        for m in magazine:
            res[m] = 1 + res.get(m, 0)
        
        for r in ransomNote:
            if r not in res:
                return False
            if res[r] == 1:
                del res[r]
            else:
                res[r] -= 1
        return True

