# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def convert_tree(root, sum):
            """
            in order traversal, right first
            add sum to each node
            """
            # base case
            if not root:
                return [], 0
            
            # traverse right
            if root.right:
                root.right, sum = convert_tree(root.right, sum)
            
            # traverse root
            temp_val = root.val
            root.val += sum
            sum += temp_val

            # traverse left            
            if root.left:
                root.left, sum = convert_tree(root.left, sum)
                
            return root, sum
            
            
        return convert_tree(root, 0)[0]
                