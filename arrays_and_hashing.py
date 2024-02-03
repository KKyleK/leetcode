def containsDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    hash = {}
    for num in nums:
        if hash.get(num) != None:
            return True
        hash.update({num:num})
    return False

#print(containsDuplicate([0,4,5,0,3,6]))

def isAnagram(s, t):
    string_1 = list(s)
    string_2 = list(t)

    for s in string_1:
        counter = 0
        found = False
        while counter < len(string_2):
            if s == string_2[counter]:
                string_2.pop(counter)
                found = True
                break
            counter = counter+1
        if not found:
            return False
    
    if len(string_2) == 0:
        return True
    else:
        return False


#1. Pick the first string, add it to an array.
#2. Search through the array of strings, add it to the array.
#3. Repeat.
def groupAnagram(strs):
    output = [] #will be an array of arrays.
    counter = 0
    while counter < len(strs):
        addition = []
        addition.append(strs[counter])
        strs.pop(counter)
    
        inner_counter = 0
        while inner_counter < len(strs):
            if isAnagram(addition[0],  strs[inner_counter]):
                addition.append(strs[inner_counter])
                strs.pop(inner_counter)
                inner_counter = inner_counter-1
            inner_counter = inner_counter+1
        output.append(addition)

    return output
strs = ["eat","tea","tan","ate","nat","bat"]
strs = [""]
#strs = ["a"]
print(groupAnagram(strs))
#print(isAnagram("", ""))

def topKFrequent(nums, k):
    #Construct dictionary that has key:frequency.
    store = {}
    for n in nums:
        if store.get(n) != None:
            store[n] = store[n] + 1
        else:
            store.update({n:1})

    #Take all of the keys. Remove the smallest ones over and over again until the array has length k.
    output = list(store.keys())
    while len(output) > k:
        smallest = output[0]
        for i in output:
            if store[i] < store[smallest]:
                smallest = i
        output.remove(smallest)
    return output



print(topKFrequent([1,2,3,4,5,6,6],2))
