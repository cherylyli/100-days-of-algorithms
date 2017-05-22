# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def appendToCache(self, cache, branches, curr):
        while curr:
            cache.append(curr.val)
            if curr.right:
                branches.append(curr)
            curr = curr.left
            
            
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.cache = []
        self.branches = []
        self.appendToCache(self.cache, self.branches, root)


    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.cache)>0

    def next(self):
        """
        :rtype: int
        """
        nextElem = self.cache.pop()
        
        # if nextElem was a branch
        if len(self.branches) > 0 and nextElem == self.branches[-1].val:
            curr_node = self.branches.pop().right
            self.appendToCache(self.cache, self.branches, curr_node)
            
        return nextElem
                

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())