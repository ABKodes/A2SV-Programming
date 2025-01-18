# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        count = defaultdict(int)
        def dfs(root):
            if root:
                count[root.val] += 1
                dfs(root.left)
                dfs(root.right)
        dfs(root)
        maxFreq = max(count.values())
        return [key for key,value in count.items() if value == maxFreq]