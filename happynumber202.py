class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        visited = set()

        while n not in visited:
            visited.add(n)
            n = self.squareOfNums(n)

            if n == 1:
                return True
        return False
        
    def squareOfNums(self, n):
        output = 0
        while n:
            digit = n % 10
            digit = digit ** 2
            output += digit
            n = n // 10
        return output
