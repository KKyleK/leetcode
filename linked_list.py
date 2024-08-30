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