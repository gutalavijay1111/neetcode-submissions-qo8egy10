# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        max_found = float("-inf")
        
        def dfs(node, max_found):
            good = 0
            if not node:
                return 0

            if node.val >= max_found:
                max_found = max(max_found, node.val)
                good += 1

            good += dfs(node.left, max_found)
            good += dfs(node.right, max_found)

            return good            

        return dfs(root, max_found)






