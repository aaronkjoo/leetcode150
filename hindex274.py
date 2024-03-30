class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort(reverse = True)

        for i, num in enumerate(citations):
            if i >= num:
                return i
        return len(citations)
        