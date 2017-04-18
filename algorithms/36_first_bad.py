# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n, start=1, end=None):
        """
        :type n: int
        :rtype: int
        """
        # set end var if it's undefined
        if not end:
            end = n
            
        # base case: n is 1 
        if end == start:
            if isBadVersion(end):
                return end
            else:
                return end+1
        
        # if only 2 versions
        if end-start == 1:
            if isBadVersion(start):
                return start
            else:
                return end
         
        next = (end+start)//2
        # if mid is bad version, look ahead
        if isBadVersion(next):
            return self.firstBadVersion(n, start, next)
            
        # else look behind
        else:
            return self.firstBadVersion(n, next, end)
        