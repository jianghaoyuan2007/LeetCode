from collections import deque


class Solution:

    def minDepth(self, root):
        if not root:
            return 0
        queue = deque()
        queue += [root]
        depth = 1
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if not node.left and not node.right:
                    return depth
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            depth += 1
        return depth

