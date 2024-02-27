#704: Binary search.
def search(nums, target):
    offset=0
    #Binary search: If my number is greater then half, search in greater half of the array.
    while len(nums) > 0:
        half = (len(nums))//2
        if target==nums[half]:
            return half+offset
        elif target > nums[half]:
            offset+=half+1
            nums = nums[half+1:]
        else:
            nums = nums[0:half]
    return -1

# nums=[-1,0,3,5,9,12]
# target=9
# print(search(nums,target))

#74: Search a 2D Matrix
def searchMatrix(matrix, target):
    #Find the row that the element resides on. That is: the current column should be smaller then the item.
    row_found=False
    start=0
    end=len(matrix)-1
    while not row_found and start!=end:
        mid = (end+start)//2
        if matrix[mid][0] == target:
            return True
        elif matrix[mid][0] > target:
            end=mid
        else:
            if matrix[mid+1][0] > target:
                row_found=True
            else:
                start = mid+1
    if not row_found:
        if matrix[end][len(matrix[end])-1] < target:
            return False
        else:
            mid=end
    #Perform a binary search on the resulting array.
    arr = matrix[mid]
    start=0
    end = len(arr)-1
    while start<end:
        mid = ((end+start)//2)
        if target==arr[mid]:
            return True
        elif target < arr[mid]:
            end=mid-1
        else:
            start=mid+1
    if arr[start] == target:
        return True
    return False

matrix=[[-9,-8,-8],[-5,-3,-2],[0,2,2],[4,6,8]]
# print(searchMatrix(matrix,15))

import math
#875: Koko eating bananas.
def minEatingSpeed(piles, h):
    #We know a few things:
    #The eating speed will have to be: 0 < max(piles)
    #Perform a binary search on that?
    piles.sort()
    max=piles[-1]

    start = 1
    end = max
    slowest_rate=max

    while start < end:
        eat_rate = (start+end)//2
        print("eat rate:" + str(eat_rate))
        #All bananas eaten successfully. Attempt to eat slower.
        if (eat_banana(piles, h, eat_rate)):
            if eat_rate < slowest_rate:
                slowest_rate=eat_rate
            end = eat_rate-1

        else:
            start = eat_rate+1
    if start==end:
        eat_rate=end
        if (eat_banana(piles, h, eat_rate)):
            if eat_rate < slowest_rate:
                slowest_rate=eat_rate

    return slowest_rate

def eat_banana(piles, h, eat_rate):
    curr_pile=0
    while curr_pile < len(piles):
        if piles[curr_pile] != 0:
            h -= math.ceil(piles[curr_pile] / eat_rate)
        curr_pile+=1
    if h>=0:
        return True
    else:
        return False

# print(minEatingSpeed([3,6,7,11], 8))
# print(minEatingSpeed([30,11,23,4,20], 5))
# print(minEatingSpeed([30,11,23,4,20], 6))

# print(minEatingSpeed([312884470],968709470))


#153: Find minimum in rotated sorted array.
#From testing, the deque here is actually slower on average then just using the list.
#This is probably because of the initialization time required to create the deque object,
#as well as importing it from the collections library.
from collections import deque
def findMin(nums):

    nums_deque = deque(nums) #This should be faster.
    while nums_deque[0] > nums_deque[-1]:
        first = nums_deque.popleft()
        nums_deque.append(first)
    return nums_deque[0]

# print(findMin([4,5,6,7,0,1,2]))

#33: Sorted array search.
#Very similar to the problem above. We will un-rotate the array
#and then perform a binary search for the target.
def search(nums, target):
    rotations=0
    while nums[0] > nums[-1]:
        first = nums.pop(0)
        nums.append(first)
        rotations+=1
    #An array of length one breaks the modulo code below, so check that case here.
    if (len(nums)==1):
        if target==nums[0]:
            return 0
        else:
            return -1
    #Perform binary search on the array.
    start=0
    end=len(nums)-1
    while start < end:
        half = ((start+end)//2)
        if nums[half] == target:
            return ((half+rotations) % (len(nums)))
        elif nums[half] < target:
            start=half+1
        else:
            end=half-1
    if nums[start] == target:
        return ((start+rotations) % (len(nums)))
    return -1

# print(search([1,3], 3))

#981: Time Based Key-Value Store.
class TimeMap:
    def __init__(self):
        self.dict={}

    def set(self, key, value, timestamp):
        arr = self.dict.get(key)
        #Key already exists. Add timestamp using binary search.
        if arr:
            end = len(arr)-1
            start = 0
            while start < end:
                mid = (end+start) //2
                if arr[mid][1] < timestamp:
                    start = mid+1
                else:
                    end = mid-1
            arr.insert(start+1,(value,timestamp))
        else:
            self.dict[key] = [(value,timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        #Key exists. Find the tuple that contains the given timestamp. (Or the last timestamp)
        if self.dict.get(key):
            arr = self.dict[key]
            start = 0
            end = len(arr)-1
            while start < end:
                mid = (end+start) //2
                if arr[mid][1] == timestamp:
                    return arr[mid][0]
                elif arr[mid][1] < timestamp:
                    start=mid+1
                else:
                    end = mid-1
            if arr[start][1] == timestamp:
                    return arr[start][0]
            if arr[start][1] < timestamp:
                return arr[start][0]
            else:
                if arr[start-1][1] < timestamp:
                    return arr[start-1][0]
                else:
                    return ""
        else:
            return ""

# map = TimeMap()
# map.set("love","high",10)
# map.set("love","low",20)
# map.get("love",5)
# map.get("love",10)
# map.get("love",15)
# map.get("love",20)
# map.get("love",25)