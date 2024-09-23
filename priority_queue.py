#703: Kth Largest Element in a Stream.
#
# Here we need to maintain a list of test scores, and always have the kth largest score available.
class KthLargest:
    nums = []
    def __init__(self, k, nums):
        self.nums = nums
        self.nums.sort(reverse=True)
        self.kIndex = k-1

    #Adds the new value, returns the kth largest element.
    def add(self, val):
        self.nums.append(val)
        self.nums.sort(reverse=True)
        if len(self.nums) > self.kIndex:
            return self.nums[self.kIndex]
        else:
            return None

# scores = KthLargest(4, [7,7,7,7,8,3])
# print(scores.add(2))
# print(scores.add(10))
# print(scores.add(9))
# print(scores.add(9))

#1046: Last Stone Weight
#Idea: until the stone array is length 1, find 2 largest (should be O(n)), then smash them.
#This is an O(n^2) solution since we need to do this process n times in the worst case.
def lastSoneWeight(stones):
    while len(stones) > 1:
        #Get the largest two stones by index
        largest = -1
        lastLargest = -1
        indexOfLargest = 0
        indexOfNextLargest = 0

        for s in range (len(stones)):
            if stones[s] > largest:
                nextLargest = largest
                indexOfNextLargest = indexOfLargest
                largest = stones[s]
                indexOfLargest = s
            elif stones[s] > nextLargest:
                nextLargest = stones[s]
                indexOfNextLargest = s
        #Smash the stones
        if stones[indexOfLargest] == stones[indexOfNextLargest]:
            #Pop the larger index first so that the second one won't get an index error.
            if indexOfLargest > indexOfNextLargest:
                stones.pop(indexOfLargest)
                stones.pop(indexOfNextLargest)
            else:
                stones.pop(indexOfNextLargest)
                stones.pop(indexOfLargest)
        else:
            stones[indexOfLargest] = stones[indexOfLargest] - stones[indexOfNextLargest]
            stones.pop(indexOfNextLargest)
    if len(stones) == 0:
        return 0
    else:
        return stones[0]

# stones = [2,2]
# print(lastSoneWeight(stones))

#973: K Closest points to origin
#Given an array of points [x,y] return the K closes points to the origin, where distance = sqrt(x^2 + y^2)
#Idea: calculate the distance of each point. Store in a tuple that looks like: (distance, point) Then pop K elements from the priority queue. (Python's priority queue automatically uses the first element in the tuple for ordering, so distance is the first element in the tuple)
import math
#heapq is a module that acts as a priority queue.
import heapq
def kClosest(points, k):
    priorityQueue = []
    for p in points:
        distanceSquared = (p[0]**2) + (p[1] **2)
        point = (math.sqrt((p[0]**2) + (p[1] **2)), p)
        heapq.heappush(priorityQueue, point)

    toReturn = []

    for p in range(k):
        (distance, point) = heapq.heappop(priorityQueue)
        toReturn.append(point)
    return toReturn

# points = [[1,3],[-2,2], [10,10], [1,1], [0,0], [3,1]]
# k = 2
# print(kClosest(points, k))

#215: Kth largest elements in an array.
#Simplest solution is to sort the array and return the kth largest element.
#Another solution is to multiply each number by -1 (since heapq gives you the smallest elements), then pop elements k times.
#Another solution, pop elements from the heapq len(nums) - k times.
def findKthLargest(nums, k):
    #Without this, nums is not a heap, and the first call of heappop will return the first element from the array, before converting it to a heap.
    heapq.heapify(nums)
    for i in range(len(nums)-k+1):
        num = heapq.heappop(nums)
    return num