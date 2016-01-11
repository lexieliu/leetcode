# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])
        root = TreeNode(0)
        nodestack = [root]
        leftindexstack = [0] 
        rightindexstack = [len(nums)-1]
        while nodestack:
            currnode = nodestack.pop()
            left = leftindexstack.pop()
            right = rightindexstack.pop()
            mid = (left+right)/2
            currnode.val = nums[mid]
            if left <= mid-1:
                currnode.left = TreeNode(0)
                nodestack.append(currnode.left)
                leftindexstack.append(left)
                rightindexstack.append(mid-1)
            if right >= mid+1:
                currnode.right = TreeNode(0)
                nodestack.append(currnode.right)
                leftindexstack.append(mid+1)
                rightindexstack.append(right)
        return root
            
