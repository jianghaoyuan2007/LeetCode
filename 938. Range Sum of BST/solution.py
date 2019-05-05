class Solution:
    def rangeSumBST(self, root, left, right):
        if not root:
            return 0
        left_tree_sum = 0
        right_tree_sum = 0
        if root.val >= left:
            left_tree_sum = self.rangeSumBST(root.left, left, right)
        if root.val <= right:
            right_tree_sum = self.rangeSumBST(root.right, left, right)
        if left <= root.val <= right:
            root_node = root.val
        else:
            root_node = 0
        return left_tree_sum + root_node + right_tree_sum

