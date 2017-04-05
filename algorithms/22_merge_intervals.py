# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) == 0:
            return []
        # sort based on first element in arr
        positions = []
        startPositions = {}
        for interval in intervals:
            # if the start is already present, save the one with the higher end
            if interval.start in startPositions:
                if interval.end > startPositions[interval.start]:
                    startPositions[interval.start] = interval.end
            else:
                startPositions[interval.start] = interval.end
        
        
        merged_intervals = []
        startPositions = sorted(startPositions.items())
        curr = list(startPositions.pop(0))
        
        # for each key/value pair in startPositions
        for s, e in startPositions:
            if s <= curr[1]:
                if e > curr[1]:
                    curr[1] = e
            else:
                merged_intervals.append(curr[:])
                curr = [s, e]
            
        merged_intervals.append(curr[:])
        return merged_intervals

            
