# Реализовать обход дерева post-order. Сначала левое, потом правое поддерево, в последнюю очередь корень
# Submit прошел
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ans = []
        def helper(node :Optional[TreeNode]):

            if node.left:
                helper(node.left)
            if node.right:
                helper(node.right)
            ans.append(node.val)
        helper(root)
        return ans