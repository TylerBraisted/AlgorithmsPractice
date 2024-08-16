'''
    BST Search:
    Given the root of a binary search tree (BST) and an integer val.
    Find the node in the BST that the node's value equals val and return 
    the subtree rooted with that node. If such a node does not exist, return null.

    Time: 
    - Best Case: O(log(N)), when the tree is well balanced and where N is the number of nodes in the tree
    - Worst Case: O(N), when the tree is skewed and where N is the number of nodes in the tree
    Space:
    - Best Case: O(log(N)), when the tree is well balanced and where N is the number of nodes in the tree
    - Worst Case: O(N), when the tree is skewed and where N is the number of nodes in the tree
    
    This is the definition for a binary tree node.
    class TreeNode:
      def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
'''
def SearchBST(self, root, val):
  if not root:
    return None
  if root.val == val:
    return root
  if root.val < val:
    return self.searchBST(root.right, val)
  if root.val > val:
    return self.searchBST(root.left, val)
