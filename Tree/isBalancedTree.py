class Solution:
    def isBalanced(self, root):
        if not root:
            return True

        if self.isBalanced(root.left) and self.isBalanced(root.right) and abs(self.depth(root.left)-self.depth(root.right))<2:
            return True

        return False

    def depth(self,node):

        if node is None:
            return 0
        return 1 + max(self.depth(node.left),self.depth(node.right))
