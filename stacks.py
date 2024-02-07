#The Python Collections library has a deque which is a list that is designed for use as a stack or queue.
#List methods:
#append(adds to end)
#pop(removes item at given index)
#insert(inserts at any index)
#Deque extra methods:
#append_left()
#popleft()  Note that deque.pop ALWAYS removes from the right side opposed to the list.

#For now, using just list methods, and I will swap to a deque if I need the added performance.

from collections import deque #without this I was beating 19%, now it's beating 71%
#
#20
def isValid(s):
    open_brace = ['(', '{', '[']
    close_brace = [')', '}', ']']
    stack = deque()
    for i in s:
        if i in open_brace:
            stack.append(i)
        else:
            if len(stack) == 0:
                return False
            end = stack.pop() #By default, pop returns the last element.
            if open_brace.index(end) != close_brace.index(i):
                return False
    if len(stack)!=0:
        return False
    return True

test = "()[]{}"
print(isValid("(]"))