import collections
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = collections.defaultdict(list)
        # initialize a list of 26 zeroes for each letter in alphabet
        for s in strs: 
            count = [0] * 26
            
            for c in s:
                count[ord(c) - ord("a")] += 1

            res[tuple(count)].append(s)
        return res.values()
        
        

solution = Solution()
print(solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))