class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


#206: Reverse linked list
#Idea: Recurse to the tail, then append each element to a linked list.
def reverseList(self, head, newList):
    if head is None:
        return None
    output = reverseListHelper(head, output=[])
    newHead = None
    for i in output:
        if newHead== None:
            newHead = ListNode(i)
            prev = newHead
        else:
            current = ListNode(i)
            prev.next = current
            prev = current

    return newHead


def reverseListHelper(self, current, output=[]):
    if current.next is not None:
        reverseListHelper(current.next, output)
    output.append(current.val)
    return output

#21: Merge two sorted lists
#Idea: Start from the left of both linked lists. Add the smaller node, traverse on that list.
def mergeTwoLists(list1, list2):
    if (list1 is None) and (list2 is None):
        return None
    newHead = None
    newListCurrent = newHead
    newListPrevious = None
    list1Current = list1
    list2Current= list2

    while (list1Current is not None) or (list2Current is not None):
        #Both lists have elements to traverse.
        if (list1Current is not None) and (list2Current is not None):
            if list1Current.val <= list2Current.val:
                toInsert = list1Current.val
                list1Current = list1Current.next
            else:
                toInsert = list2Current.val
                list2Current = list2Current.next
        elif (list1Current is not None) and (list2Current is None):
            toInsert = list1Current.val
            list1Current = list1Current.next
        else:
            toInsert = list2Current.val
            list2Current = list2Current.next

        #Insert the value into the new list
        if(newHead is None):
            newHead = ListNode(toInsert)
            newListPrevious = newHead
        else:
            newListCurrent = ListNode(toInsert)
            newListPrevious.next = newListCurrent
            newListPrevious = newListCurrent
    return newHead

#143: Reorder list
# Reorder the list: L0 → L1 → … → Ln - 1 → Ln     To     L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2
# Without making a new list (Modify the reference)
#
# Idea: Start with the first node, make it point to the last node in the list.
# Repeat until the node doesn't have a next.
def reorderList(head):
    if head.next == None:
        return head

    #Store nodes in order to easily have access to the last and second last nodes.
    last=[]
    fullTraverse=head
    lastNode =None
    while fullTraverse != None:
        last.append(fullTraverse)
        fullTraverse=fullTraverse.next

    currentNode = head
    while currentNode.next is not None:

        if lastNode is None:
            lastNode = last.pop()
            secondLast = last.pop()
        else:
            lastNode = secondLast
            secondLast = last.pop()

        oldNext = currentNode.next
        currentNode.next = lastNode
        if (lastNode != oldNext):
            lastNode.next = oldNext
            secondLast.next = None

        currentNode = oldNext

    return head

def printLinkedList(head):
    currNode = head
    while currNode is not None:
        print(currNode.val)
        currNode=currNode.next
    return



# one = ListNode(1)
# two = ListNode(2)
# three = ListNode(3)
# four = ListNode(4)
# one.next = two
# two.next = three
# three.next = four
# # printLinkedList(one)

# reorderList(one)
# printLinkedList(one)

#19: Remove Nth Node From End of List:
# Idea: Perform one traversal to get the length of the linked list.
# Perform a second traversal to the node to be eliminated.
def removeNthFromEnd(head, n):
        current=head
        distance=0
        while current!=None:
            distance+=1
            current = current.next
        #List is one node long, remove it.
        if distance == 1:
            return None

        #n starts at 1.
        distanceToRemove = distance-n

        counter = 0
        current = head
        prev=current
        while counter < distanceToRemove:
            prev=current
            current = current.next
            counter+=1

        #Removing from head.
        if (current == prev):
            head = head.next
        prev.next = current.next
        current.next = None
        return head

#138: Copy List with Random Pointer
#Idea: Without the random pointer, I would use a current and previous pointer to traverse the list,
#Creating new nodes as needed.
#
#If I store all of the elements in an array, I can use indicies to create the random pointers.
def copyRandomList(head):
    if head is None:
        return None

    #Create the new list while storing the old one in an array.
    #Usually we need a prev pointer to get the .next connection right, but we don't this time since we are storing them in an array.
    oldList=[]
    newList=[]
    current = head
    while current is not None:
        oldList.append(current)
        newList.append(ListNode(current.val))
        current = current.next

    #Add next pointers
    for i in range(len(newList)-1):
        newList[i].next = newList[i+1]

    for i in range(len(newList)):
        randomNode = oldList[i].random
        if randomNode is None:
            newList[i].random = None
        else:
            #Find the random node's indicie.
            index=0
            for k in range(len(oldList)):
                if oldList[k] == randomNode:
                    index=k
            newList[i].random = newList[index]

    return newList[0]

#138: Add two numbers:
def addTwoNumbers(l1, l2):
    newList = None
    newListCurrent = newList
    l1Current = l1
    l2Current = l2
    carry=0

    while l1Current or l2Current:
        if l1Current and l2Current:
            sum = l1Current.val+l2Current.val
        elif l1Current and not l2Current:
            sum = l1Current.val
        else:
            sum = l2Current.val
        sum+=carry
        carry=0

        if (sum >= 10):
            #Can just subtract here, can never get a sum of 20.
            sum = sum-10
            carry=1
        #insert at head
        if newList == None:
            newList = ListNode(sum)
            newListCurrent = newList
        else:
            newListCurrent.next = ListNode(sum)
            newListCurrent = newListCurrent.next
        if l1Current:
            l1Current = l1Current.next
        if l2Current:
            l2Current = l2Current.next
    #There could be a remaining carry to consider.
    if carry == 1:
        newListCurrent.next = ListNode(carry)
    return newList

#141: Linked List cycle
#Find if there is a cycle in a linked list.
#Simple idea: Use an array, store the nodes, check if a duplicate is added.
#More optimized: Use a hashmap that looks like: {nodeVal: [nodes]} and perform
#Lookup on that. Still O(n^2) in the absolute worse case where all nodes are the
#same.
#
# Hashmap version: 59ms and 19.3 MB
# Array version: 612ms and 19.1 MB.
#
# So the hashmap solution was MUCH faster and actually used almost the same memory.
def hasCycle(head):
    visited={}
    if head is None:
        return False
    current = head
    while current is not None:
        seen = visited.get(current.val)
        if seen:
            if current in seen:
                return True
            else:
                seen.append(current)
        #visited did not have any nodes
        else:
            visited.update({current.val:[current]})

        current = current.next
    return False

# one = ListNode(1)
# two = ListNode(2)
# print(hasCycle(one))
# one.next = two
# print(hasCycle(two))
# two.next = one
# print(hasCycle(one))

#146: LRU Cache
# An LRU Cache (Least recently used cache) is a fixed size cache where
# The least recently used item is removed when the cache is full and more needs to be added.
#
# Idea: Store keys and values in two data structures: a linked list, and a hashmap.
# The hashmap will cover the additions and lookups in O(1) time.
# To keep track of the least recently used node, the linked list head will represent it.
# When a value is used, that node needs to be put to the tail of the linked list in O(1) time,
# So we need a double linked list so that we can take a node out of the list from any position.

# We want to keep track of the key and value, so that the hashtable can be updated when a node needs to be
# deleted
class hashNode:
    def __init__(self, val=0, key=0, next=None, prev=None):
        self.val = val
        self.key = key
        self.next = next
        self.prev = prev
        return

class LRUCache:
    def __init__(self, capacity):
        self.cache={} #This will be: key:hashNode (where hashNode.val contains the value.)
        self.head = hashNode()
        self.tail = self.head
        self.currentCapacity=0
        self.capacity = capacity
        return

    #Every time we do a get, remove the node and add it again.
    #When we do a put on full, remove the head and add the new node.
    #Remove a node from the list.
    def removeNode(self, node):
        #Remove from the head
        if node == self.head:
            if self.head == self.tail:
                self.head = None
                self.tail = self.head
            else:
                self.head = self.head.next
                self.head.prev = None

        elif node == self.tail:
            self.tail = self.tail.prev
            self.tail.next = None

        else:
            prev = node.prev
            next = node.next
            prev.next = next
            next.prev = prev
        return

    #Add a node to the end of the list.
    def addNodeToTail(self, node):
        if self.currentCapacity == 0:
            self.head = node
            self.tail = self.head
        else:
            node.prev = self.tail
            self.tail.next = node
            node.next = None
            self.tail = node
        return

    def get(self, key):
        node = self.cache.get(key)
        #Remove the node and add it to the end.
        if node:
            self.removeNode(node)
            self.currentCapacity-=1
            self.addNodeToTail(node)
            self.currentCapacity+=1
            return node.val
        else:
            return -1

    def put(self, key, value):
        current = self.cache.get(key)
        if current:
            self.removeNode(current)
            self.currentCapacity-=1
            newNum = hashNode(value,key)
            self.cache.update({key:newNum})
            self.addNodeToTail(newNum)
            self.currentCapacity+=1

        else:
            #Check if the oldest element in the cache needs to be deleted.
            if self.currentCapacity == self.capacity:
                self.cache.pop(self.head.key)
                self.removeNode(self.head)
                self.currentCapacity -=1

            #Add the new element.
            newNum = hashNode(value, key)
            self.cache.update({key:newNum})
            self.addNodeToTail(newNum)
            self.currentCapacity +=1
        return

c = LRUCache(1)
c.put(2,1)
print(c.get(2))

# c = LRUCache(1)
# c.put(2,1)
# print(c.get(2))

# c = LRUCache(3)
# c.put(1,1)
# c.put(2,2)
# c.put(3,3)
# c.put(4,4) # (2,2) (3,3) (4,4)

# print(c.get(4))
# print(c.get(3))
# print(c.get(2)) #(4,4) (3,3) (2,2)
# print(c.get(1))
# c.put(5,5) #(3,3) (2,2) (5,5)
# print(c.get(1))
# print(c.get(2)) #(3,3) (5,5) (2,2)
# print(c.get(3))
# print(c.get(4))
# print(c.get(5))