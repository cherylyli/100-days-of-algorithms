class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # if root doesn't exist
        if not root:
            return
        
        if root.val == p.val:
            return p
            
        if root.val == q.val:
            return q
            
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
            
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        
        return root
        