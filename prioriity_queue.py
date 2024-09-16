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

scores = KthLargest(4, [7,7,7,7,8,3])
print(scores.add(2))
print(scores.add(10))
print(scores.add(9))
print(scores.add(9))