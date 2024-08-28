#78: Subsets
#Return the power set, that is the list of all possible sets given an input set.
#
# Idea: An additional set can be constructed as long as it's length is smaller than len(nums). Add a number in, and attempt to make any combinations with it that are already in the set.
#
def subsets(nums):
    powerset=[]
    for i in range(len(nums)):
        powerset.append([nums[i]])
        #Attempt to add additional sets by adding the current number
        #To any sets before.
        powersetLength = len(powerset)-1
        for j in range(powersetLength):
            arr=[]
            for num in powerset[j]:
                arr.append(num)
            arr.append(nums[i])
            powerset.append(arr)

    powerset.append([])
    return powerset

#powerset of: 1,2,3,4 using my algo:
# [1] , [2], [1,2], [3], [1,3] [2,3], [1,2,3], [4], [1,4], [2,4], [1,2,4], [3,4], [1,3,4], [2,3,4], [1,2,3,4]
# Seems great!
print(subsets([1,2,3]))