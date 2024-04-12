# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode:
        #if not preorder or not inorder:
        #    return None
        
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        #print(root)
        #print(mid)
        #print(preorder[1:mid+1])
        #print(inorder[:mid])
        #print(preorder[mid + 1:])
        #print(inorder[mid + 1:])


solution = Solution()
print(solution.buildTree([3,9,20,15,7], [9,3,15,20,7]))