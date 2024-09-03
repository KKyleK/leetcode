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



one = ListNode(1)
two = ListNode(2)
three = ListNode(3)
four = ListNode(4)
one.next = two
two.next = three
three.next = four
# printLinkedList(one)

reorderList(one)
printLinkedList(one)

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