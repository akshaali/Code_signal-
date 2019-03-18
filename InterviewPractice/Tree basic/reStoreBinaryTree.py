"""
Note: Your solution should have O(inorder.length) time complexity, since this is what you will be asked to accomplish in an interview.

Let's define inorder and preorder traversals of a binary tree as follows:

Inorder traversal first visits the left subtree, then the root, then its right subtree;
Preorder traversal first visits the root, then its left subtree, then its right subtree.
For example, if tree looks like this:

    1
   / \
  2   3
 /   / \
4   5   6
then the traversals will be as follows:

Inorder traversal: [4, 2, 1, 5, 3, 6]
Preorder traversal: [1, 2, 4, 3, 5, 6]
Given the inorder and preorder traversals of a binary tree t, but not t itself, restore t and return it.

Example

For inorder = [4, 2, 1, 5, 3, 6] and preorder = [1, 2, 4, 3, 5, 6], the output should be
restoreBinaryTree(inorder, preorder) = {
    "value": 1,
    "left": {
        "value": 2,
        "left": {
            "value": 4,
            "left": null,
            "right": null
        },
        "right": null
    },
    "right": {
        "value": 3,
        "left": {
            "value": 5,
            "left": null,
            "right": null
        },
        "right": {
            "value": 6,
            "left": null,
            "right": null
        }
    }
}
For inorder = [2, 5] and preorder = [5, 2], the output should be
restoreBinaryTree(inorder, preorder) = {
    "value": 5,
    "left": {
        "value": 2,
        "left": null,
        "right": null
    },
    "right": null
}
"""

#
# Definition for binary tree:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def restoreBinaryTree(inorder, preorder):
  if not preorder:
    return None
  root = Tree(preorder[0]) #first element gives the root of tree 
  i = inorder.index(preorder[0]) # finding the index upto which the left tree is .
  root.left = restoreBinaryTree(inorder[:i], preorder[1:i+1]) #recurrsive calls to calculate left branch
  root.right = restoreBinaryTree(inorder[i+1:],preorder[i+1:]) # same here to calculate right branch 
  return root
