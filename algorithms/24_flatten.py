class Vector2D(object):

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        # remove empties
        self.vec = []
        for vec in vec2d:
            if len(vec) > 0:
                self.vec.append(vec)
        

    def next(self):
        """
        :rtype: int
        """
        # return first element of first element of self.vec
        if len(self.vec[0]) == 0:
            self.vec.pop(0)
        elif len(self.vec[0]) == 1:
            return self.vec.pop(0)[0]
        return self.vec[0].pop(0)
        

    def hasNext(self):
        """
        :rtype: bool
        """
        if len(self.vec) == 0:
            return False
        elif len(self.vec) == 1 and len(self.vec[0]) == 0:
            return False
        return True
        
        

# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())