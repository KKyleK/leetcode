class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def print_all(root, vals=[]):
    if root is not None:
        print(root.val)
        vals.append(root.val)
        print_all(root.right, vals)
        print_all(root.left, vals)
    return vals

def printt(root):
    arr = print_all(root)
    return arr

#Add a leaf to a tree. Not re-balancing for now.
#I thought that traversing to the none leaf and updating that into a real leaf
#would work since the real leaf would still be connected to the tree with the .right
#or .left, but that isn't the case. Must add values to the tree by updating .right and .left
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

# bot_left = TreeNode(1)
# bot_mid_left = TreeNode(3)
# bot_mid_right = TreeNode(6)
# bot_right= TreeNode(9)
# left = TreeNode(2,bot_left,bot_mid_left)
# right= TreeNode(7,bot_mid_right,bot_right)
# root = TreeNode(4,left,right)

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
#Diameter is the largest distance between two nodes in the tree.
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
#Idea: For each node, compute the depth of the node's right and left nodes. If they are not within one of each other,
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

#100: Same tree.
# Idea: Add both trees into an array. Check if the elements of the array are ident
def isSameTree(p,q):
    toVisitTree1 = []
    toVisitTree1.append(p)
    toVisitTree2 = []
    toVisitTree2.append(q)
    #Check base case that one or both of the trees are empty.
    if p is None:
        if q is None:
            return True
        else:
            return False
    if q is None:
        if p is None:
            return True
        else:
            return False

    while len(toVisitTree1) > 0 and len(toVisitTree2) > 0:
        node1 = toVisitTree1.pop()
        node2 = toVisitTree2.pop()
        if node1.val != node2.val:
            return False
        #Traverse the trees.
        if node1.right is not None:
            toVisitTree1.append(node1.right)
        if node1.left is not None:
            toVisitTree1.append(node1.left)
        if node2.right is not None:
            toVisitTree2.append(node2.right)
        if node2.left is not None:
            toVisitTree2.append(node2.left)

        #Check that each tree contains the same null nodes.
        if (node1.right is None and node2.right is not None) or (node1.right is not None and node2.right is None):
            return False
        if (node1.left is None and node2.left is not None) or (node1.left is not None and node2.left is None):
            return False

    if len(toVisitTree1) > 0 or len(toVisitTree2) > 0:
        return False
    return True

#572: Subtree of another tree.
#Idea: for each node of the main tree, run isSameTree on the node and the subtree.
def isSubtree(root, subRoot):
    if root is None:
        if subRoot is None:
            return True
        else:
            return False
    toVisit = []
    toVisit.append(root)
    while len(toVisit) > 0:
        currentNode = toVisit.pop()
        if isSameTree(currentNode, subRoot):
            return True
        else:
            if currentNode.right is not None:
                toVisit.append(currentNode.right)
            if currentNode.left is not None:
                toVisit.append(currentNode.left)
    return False

#235: Lowest common ancestor of a binary search tree.

#the lowest common ancestor of p and q is the node t that has both p and q as descendants.
#Idea: Traverse to p and q. Maintain a list of nodes that were traversed to find p and q.
#Return the last value from the smaller list which is also present in the larger list.

#returns the route followed in a BST to find a given target node.
#Assumes the target exists in the tree.
#Also assumes that all values in the tree are unique.
def findNode(root, target):
    route=[]
    if target.val==root.val:
        return [target.val]
    currentNode = root
    while currentNode.val != target.val:
        route.append(currentNode.val)
        if target.val < currentNode.val:
            currentNode = currentNode.left
        else:
            currentNode = currentNode.right
    route.append(target.val)
    return route

def lowestCommonAncestor(root, p, q):
    pRoute = findNode(root, p)
    qRoute = findNode(root,q)

    counter = (min(len(pRoute), len(qRoute))) - 1
    found = False
    while not found:
        if len(pRoute) < len(qRoute):
            value = pRoute[counter]
            if value in qRoute:
                found=True
        else:
            value = qRoute[counter]
            if value in pRoute:
                found=True
        counter-=1
    #Find and return the node corresponding to the target value.
    currentNode = root
    while True:
        if currentNode.val == value:
            return currentNode
        if value < currentNode.val:
            currentNode = currentNode.left
        else:
            currentNode = currentNode.right

#102: Binary Tree Level Order Traversal.
#idea: Perform a breadth first traversal of the tree. Instead of using a single
#queue where we pop an element, and add it's children to the end of the queue,
#we use a 2d array, adding all of the children from each previous array to the next
#element of the array.
def levelOrder(root):
    toVisit=[[]]
    if root is not None:
        toVisit=[[root]]
    else:
        return []

    counter = 0
    while len(toVisit[counter]) != 0:
        nextLevel = []
        for node in toVisit[counter]:
            if node.left is not None:
                nextLevel.append(node.left)
            if node.right is not None:
                nextLevel.append(node.right)
        toVisit.append(nextLevel)
        counter+=1
    #Now we have the nodes in order in toVisit. Convert them to their values.
    nodeValues=[[]]
    for i in toVisit:
        add=[]
        for j in i:
            add.append(j.val)
        if len(nodeValues[0]) == 0:
            nodeValues[0] = add
        else:
            if len(add) != 0:
                nodeValues.append(add)
    return nodeValues

#199: Binary Tree Right Side View.
#Idea: Use the levelOrder function to return an array of the values at each level of the tree.
#Then take the right most element from each level of the tree.
def rightSideView(root):
    levelOrderValues = levelOrder(root)
    if len(levelOrderValues) == 0:
        return []
    rightSideView = []
    for treeRow in levelOrderValues:
        rightSideView.append(treeRow[-1])
    return rightSideView

#1448: Count Good Nodes in Binary Tree.
#Idea: Perform a search on the tree. If the child of nodes is greater, increment the count,
#and add that node to the list of nodes that need to be visited. If the node is smaller,
#don't increment the count. Change the value of the node to be it's parent, then add it.
def goodNodes(root):
    toVisit=[]
    goodNodes = 0
    if root is None:
        return 0
    toVisit.append(root)
    goodNodes+=1
    while len(toVisit) > 0:
        currentNode = toVisit.pop()
        if currentNode.left is not None:
            if currentNode.left.val >= currentNode.val:
                goodNodes+=1
            else:
                currentNode.left.val = currentNode.val
            toVisit.append(currentNode.left)
        if currentNode.right is not None:
            if currentNode.right.val >= currentNode.val:
                goodNodes+=1
            else:
                currentNode.right.val = currentNode.val
            toVisit.append(currentNode.right)
    return goodNodes

#98: Validate Binary search tree.
#Idea: Perform an in order traversal of the tree. Check that the values are in ascending order.
#O(n) since we are visiting each node once, and then traversing an array of n elements, so that's 2n operations or O(n)
def isValidBST(root):
    #Generate a list of the nodes resulting from an in order traversal.
    inOrderTraversal=[]
    backTrack=[] #Stack
    currentNode=root

    while len(backTrack) > 0 or currentNode is not None:
        while currentNode is not None:
            backTrack.append(currentNode)
            currentNode = currentNode.left

        currentNode = backTrack.pop()
        inOrderTraversal.append(currentNode.val)
        currentNode = currentNode.right

    #Check that the in order traversal is in ascending order.
    if len(inOrderTraversal) == 1:
        return True
    previous = inOrderTraversal[0]
    counter=1
    while counter < len(inOrderTraversal):
        if inOrderTraversal[counter] <= previous:
            return False
        previous = inOrderTraversal[counter]
        counter = counter+1
    return True


# In order traversal:
#    3
#   / \
#  1   2
# returns: 1, 3, 2.

#230: Kth smallest element in a BST
#Idea: Use the same in order traversal we have to return the kth smallest element.
def kthSmallest(root, k):
    #Generate a list of the nodes resulting from an in order traversal.
    inOrderTraversal=[]
    backTrack=[] #Stack
    currentNode=root

    while len(backTrack) > 0 or currentNode is not None:
        while currentNode is not None:
            backTrack.append(currentNode)
            currentNode = currentNode.left

        currentNode = backTrack.pop()
        inOrderTraversal.append(currentNode.val)
        currentNode = currentNode.right

    #Return the kth element.
    return inOrderTraversal[k-1]

#105: Construct Binary tree from preorder and in order traversal
#In order traversal: Gives us left subtree, root, right subtree.
#Pre order traversal: Gives us root, left subtree, right subtree.
def buildTree(preorder, inorder):
    #Base case: empty tree.
    if preorder is None or len(preorder) == 0:
        return None
    root = TreeNode(val=preorder[0])
    #Get the index of the root in the inorder array.
    findRoot = 0
    while findRoot < len(preorder):
        if inorder[findRoot] == root.val:
            break
        findRoot+=1
    if findRoot==0:
        root.left = None
    else:
        leftSubtreePreorder = preorder[1:findRoot+1] #skip root.
        leftSubtreeInorder = inorder[:findRoot]
        root.left=(buildTree(leftSubtreePreorder, leftSubtreeInorder))
    #No right subtree.
    if findRoot==(len(inorder)-1):
        root.right = None
    else:
        rightSubtreePreorder = preorder[findRoot+1:]
        rightSubtreeInorder = inorder[findRoot+1:]
        root.right=(buildTree(rightSubtreePreorder,rightSubtreeInorder))
    return root

preorder=[3,9,20,15,7]
inorder= [9,3,15,20,7]

root = buildTree(preorder,inorder)
arr = print_all(root)
print("HERE")
print(arr)