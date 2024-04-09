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

#Add a leaf to a tree. Not rebalancing for now.
#I thought that traversing to the none leaf and updating that into a real leaf
#would work since the real leaf would still be connected to the tree with the .right
#or .left, but that isen't the case. Must add values to the tree by updating .right and .left
#themselves.
def add_tree_node(root, val):
    if root is None:
        root= TreeNode(val, None, None)
        return root
    else:
        pointer=root
        while pointer is not None:
            if val >= pointer.val:
                if pointer.right is None:
                    pointer.right = TreeNode(val,None,None)
                    break
                else:
                    pointer = pointer.right
            else:
                if pointer.left is None:
                    pointer.left = TreeNode(val,None,None)
                    break
                else:
                    pointer = pointer.left
    return root


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

# print_all(root)
# invertTree(root)
# print_all(root)

#104: Max depth of binary tree.
def maxDepth(root, depth=0):
    #Base case: current node is null. return.
    if root is None:
        return depth
    #Recursive case: find the largest depth of the child nodes.
    right_depth = max(depth,maxDepth(root.right, depth+1))
    left_depth = max(depth,maxDepth(root.left, depth+1))
    return max(right_depth, left_depth)

#543: Diameter of binary tree.
#Diamter is the largest distance between two nodes in the tree.
def diameterOfBinaryTree(root, diameter=0):
    if root is None:
        return 0
    curr_depth = maxDepth(root.right) + maxDepth(root.left)
    left_depth = diameterOfBinaryTree(root.left)
    right_depth = diameterOfBinaryTree(root.right)
    return max(curr_depth, left_depth, right_depth)

# new_root=add_tree_node(None, 4)
# add_tree_node(new_root,7)
# add_tree_node(new_root,6)
# add_tree_node(new_root,9)
# add_tree_node(new_root,2)
# add_tree_node(new_root,3)
# add_tree_node(new_root,1)
# print(diameterOfBinaryTree(new_root))

#110: Balanced Binary tree.
#Idea: For each node, compute the depth of the node's right and left nodes. If they are not within one of eachother,
# return False. This is an O(n^2) implementation since computing the depth of a node is O(n) and we need to do that n times.
def isBalanced(root):
    if root is None:
        return True
    toVisit = []
    toVisit.append(root)
    while len(toVisit) > 0:
        current = toVisit.pop()
        leftDepth = maxDepth(current.left)
        rightDepth = maxDepth(current.right)
        if abs(leftDepth-rightDepth) > 1:
            return False
        #Check all other nodes.
        if current.left is not None:
            toVisit.append(current.left)
        if current.right is not None:
            toVisit.append(current.right)
    return True