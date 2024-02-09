import math

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
# print(isValid("(]"))


#155: Stack that must implement push, pop, top, getMin in O(1)
#The trick here is that we need to maintain a second stack that contains the
#elements with the smallest value.
class MinStack:
    def __init__(self):
        self.data = []
        self.smallest = []

    def push(self, val):
        self.data.append(val) #O(1)

        #If this is the new smallest element or a duplicate, add it to the smallest stack.
        length = len(self.smallest)
        if length ==0:
            self.smallest.append(val)
        else:
            if self.smallest[length-1] >= val:
                self.smallest.append(val)

    def pop(self):
        if len(self.data) == 0:
            return
        val = self.data.pop() #O(1)
        if self.smallest[len(self.smallest)-1] == val:
            self.smallest.pop()

    def top(self):
        length = len(self.data)
        if length == 0:
            return None
        else:
            return self.data[length-1]

    def getMin(self):
        length = len(self.smallest)
        if length == 0:
            return None
        else:
            return self.smallest[length-1]

# minStack = MinStack()
# minStack.push(-2)
# minStack.push(0)
# minStack.push(-3)
# print(minStack.getMin()) # return -3
# minStack.pop()
# print(minStack.top()) # return 0
# print(minStack.getMin()) # return -2

#150: 
#Division operations are floored.
def evalRPN(tokens):
    stack = []
    operations = ['+', '-', '*','/']
    for i in tokens:
        if i in operations:
            operand1 = stack.pop()
            operand2 = stack.pop()
            # print(str(operand2) + ' ' + i + ' '+ str(operand1))
            if i == '+':
                value = operand2+operand1
            elif i == '-':
                value = operand2-operand1
            elif i == '*':
                value = operand2*operand1
            else:
                value = (operand2/operand1)
                if value < 0 and value != math.floor(value):
                    value+=1
                value = int(math.floor(value))
            stack.append(value)
        else:
            stack.append(int(i))
    return stack.pop()

# tokens = ["2","1","+","3","*"]
# tokens = ["4","13","5","/","+"]
# tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
# tokens = ["4","-2","/","2","-3","-","-"]
# print(evalRPN(tokens))