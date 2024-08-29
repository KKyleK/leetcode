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
# print(subsets([1,2,3]))

#39: Combination Sum:
# Given an array of numbers, return all of the possible ways to add to a target sum. Numbers can be reused.
#
#Idea: For each element in candidates, attempt to add it. If the sum goes over, don't add it.
def combinationSum(candidates, target):
    #Optimization: Remove elements from candidates that are larger than target:
    counter=0
    while counter < len(candidates):
        if candidates[counter] > target:
            candidates.pop(counter)
            counter-=1
        counter+=1
    #Optimization: Store the frequency of solutions so that they don't need to be re computed.
    frequencyTable={} #counter, [frequency]

    #Default arguments need to be specified or they will be reused in subsequent calls (Ie the first solution will bleed into the second one.)
    solutions = combinationSumHelper(candidates, target, output=[], current=[], currentSum=0)
    #Remove duplicates
    counter = 0
    while counter < (len(solutions)-1):
        if (solutions[counter] == []):
            counter+=1
            continue
        frequency = frequencyTable.get(counter)
        if (not frequency):
            frequency = getFrequency(solutions[counter], candidates)
            frequencyTable.update({counter:frequency})
        current = counter+1
        while current < len(solutions):
            if (solutions[current] == []):
                current+=1
                continue
            currentFrequency = frequencyTable.get(current)
            if (not currentFrequency):
                currentFrequency = getFrequency(solutions[current], candidates)
                frequencyTable.update({current: currentFrequency})

            duplicate=False
            for i in range(len(frequency)):
                if (frequency[i]) != (currentFrequency[i]):
                    break
                #On last array loop, still identical
                if (i == len(frequency)-1):
                    duplicate = True
            if(duplicate):
                solutions[current] = [] #Make it empty, remove it later.

            current+=1
        counter+=1
    #Remove empty solutions
    finalSolution=[]
    for s in solutions:
        if s != []:
            finalSolution.append(s)
    return finalSolution

def getFrequency(answer, nums):
    frequency=[0] * len(nums)
    for i in answer:
        counter = 0
        while counter < len(nums):
            if nums[counter] == i:
                frequency[counter] +=1
            counter+=1
    return frequency

def combinationSumHelper(candidates, target, output=[], current=[], currentSum=0):
    #Base case: currentSum = target:
    # print("currentSum top: ")
    # print(currentSum)
    if (currentSum == target):
        #Add current by value to output.
        toAdd=[]
        for i in current:
            toAdd.append(i)
        output.append(toAdd)
        current.pop()
        return
    #Pop last output
    if (currentSum > target):
        current.pop()
        return
    #Attempt to add a new number
    for i in candidates:
        current.append(i)
        combinationSumHelper(candidates, target, output, current, currentSum+i)
    #Out of things to try, go back.
    if (len(current) > 0):
        current.pop()
    return output


#print(combinationSum([2,3,6,7], 7))
print(combinationSum([2,3,5], 8))

#Too slow! How do I make this more efficient? Remove sums above the result for one!
#Still too slow...
#Another optimization: store frequencies in a hashtable.
print(combinationSum([2,22,4,17,28,13,39,27,24,37,12,30,5,23,29,8,16,34,15,36,14,10,31], 30))