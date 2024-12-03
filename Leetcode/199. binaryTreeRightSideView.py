# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def bfs(root):
            if not root:
                return []
            queue = deque([root])
            result = []
            while queue:
                levelSize = len(queue)
                level = []
                for _ in range(levelSize):
                    current = queue.popleft()
                    level.append(current.val)
                    if current.right:
                        queue.append(current.right)
                    if current.left:
                        queue.append(current.left)
                result.append(level[0])
            return result
        return bfs(root)