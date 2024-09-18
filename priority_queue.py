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

stones = [2,2]
print(lastSoneWeight(stones))