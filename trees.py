class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def print_all(root):
    if root is not None:
        print (root.val)
        print_all(root.right)
        print_all(root.left)


#226: Invert Binary tree.
#Each node is flipped from being a left child to a right, and vice versa.

def invertTree(root):
    if (root is not None and ((root.right is not None) or (root.left is not None))):
        tmp=root.right
        root.right=root.left
        root.left=tmp

        if root.right is not None:
            invertTree(root.right)
        if root.left is not None:
            invertTree(root.left)
    return root

bot_left = TreeNode(1)
bot_mid_left = TreeNode(3)
bot_mid_right = TreeNode(6)
bot_right= TreeNode(9)

left = TreeNode(2,bot_left,bot_mid_left)
right= TreeNode(7,bot_mid_right,bot_right)
root = TreeNode(4,left,right)

print_all(root)
invertTree(root)
print()
print_all(root)

#104
def maxDepth(root, depth=0):
    #Base case: current node is null. return.
    if root is None:
        return depth
    #Recursive case: find the largest depth of the child nodes.
    right_depth = max(depth,maxDepth(root.right, depth+1))
    left_depth = max(depth,maxDepth(root.left, depth+1))
    return max(right_depth, left_depth)