#125: Valid Palindrome.

import re
def isPalindrome(str):
    lower = str.lower()
    #Remove all non-alphanumeric characters (anything that's not a character or number)
    regex_match = re.compile('[^a-zA-Z0-9]')
    new = re.sub(regex_match, '', lower)

    array = list(new)
    backwards = array.copy()
    backwards.reverse()

    print(array)
    print(backwards)

    counter = 0
    while counter < len(array):
        if array[counter] != backwards[counter]:
            return False
        counter +=1
    return True

#print(isPalindrome(" "))

#167: Two sum II. Input array sorted.
#The solution to twoSum, is to use a double for loop to check all possible combinations,
#and return the answer that way.
#I don't see how this same solution won't work, but as a bonus, we can stop searching once the values
#Become larger then the target.
def twoSum(numbers, target):

    if target < 0:
        numbers.reverse()
    i=0
    while i < len(numbers):
        if (target > 0 and numbers[i] > target) or (target < 0 and numbers[i] < target):
            break
        j=i+1
        while j < len(numbers):
            if (target > 0 and numbers[i] > target) or (target < 0 and numbers[i] < target):
                break
            if numbers[i] + numbers[j] == target:
                return [i+1,j+1]
            j+=1
        i+=1

#OK, so this is O(n^2)
#The better solution is to iterate through with two pointers. Then It's only o(n)
def twoSum(numbers, target):

    smallest = 0
    largest = len(numbers)-1
    #In the problem statement there is guarenteed a solution, so iterate until one is found.
    while True:
        sum = numbers[smallest] + numbers[largest]
        if sum == target:
            return [smallest+1,largest+1]
        elif sum > target:
            largest+=-1
        else:
            smallest+=1

nums = [2,3,4]
target = 6
# print(twoSum(nums, target))
nums = [-1,0]
target = -1
# print(twoSum(nums, target))

#15: 3Sum.
#Immediate idea:
#Choose the first number.
#Then maintain two pointers, one at the start of the list, and another at the end of the list.
#See and see if you can create a sum of 0. If you can, add it.
#Move to the next number. Go through all numbers.
#To inforce no duplicates use a set.
def threeSum(nums):
    nums.sort()
    output=set()
    i=0
    while i < (len(nums)-2):
        j=i+1
        k=len(nums)-1
        while(j!=k):
            sum = nums[i] + nums[j] + nums[k]
            if sum == 0:
                output.add((nums[i], nums[j], nums[k]))
                j+=1
            elif sum < 0:
                j+=1
            else:
                k+=-1
        i+=1
    return output

print(threeSum([-2,0,1,1,2]))
print(threeSum([0,0,0,0]))