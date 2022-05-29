# Проверить дерево на симметричность
# Submit прошел
class Solution:
    def isSymmetric(self, root):

        def helper(l_node, r_node):
            if not l_node and not r_node:
                return True
            if not l_node or not r_node:
                return False
            if l_node.val != r_node.val:
                return False
            l = helper(l_node.left, r_node.right)
            r = helper(l_node.right, r_node.left)

            return l and r

        return helper(root.left, root.right)