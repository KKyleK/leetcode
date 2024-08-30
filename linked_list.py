# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


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