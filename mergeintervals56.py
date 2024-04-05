class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """

       #intervals.sort(key = lambda i : i[0])
        intervals.sort()
        output = [intervals[0]]
        
        for start, end in intervals[1:]:
            lastEnd = output[-1][1]
            
            if start <= lastEnd:
                print(output[-1][1])
                print(lastEnd)
                print(end)
                output[-1][1] = max(lastEnd, end)
            else:
                output.append([start, end])
        return output


solution = Solution()
print(solution.merge([[1,3],[2,6],[8,10],[15,18]]))
#print(solution.merge([[1,4],[5,6]]))
# print(solution.merge([[1,3],[2,6],[8,10],[15,18]]))

"""
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
"""