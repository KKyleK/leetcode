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
# print(groupAnagram(strs))
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



# print(topKFrequent([1,2,3,4,5,6,6],2))






#238
#I have to do this in O(n) time...
#The simplist way to do this would be with a double while loop.
#For each element, go through the list and copy everything but itself.
#But that would be O(n^2).
def productExceptSelf(nums):

    result = [1]*(len(nums))
    prefixProduct = 1
    suffixProduct = 1

    for i in range (len(nums)):
        result[i] = prefixProduct
        prefixProduct = prefixProduct * nums[i]

    for i in range (len(nums)):
        result[(-1+(i*-1))] *= suffixProduct
        suffixProduct = suffixProduct * nums[(-1+(i*-1))]
    return result
    
#print(productExceptSelf([1,2,3,4]))
#Lessons: 1: O(n) can mean 2 loops over the data (or any number of loops really)
#Prefix and suffix are a common topic - Just everything before or everything after.

# 36
#Checks: Each row has no duplicates.
#        Each column has no duplicates.
#        Each 3x3 has no duplicates.
def valid_sudoku(board):
    #Check that each 3x3 has no duplicates.
    row_offset = 0
    while row_offset < 9:
        column_offset = 0
        while column_offset < 9:
            i = 0
            items = {}
            while i < 3:
                j=0
                while j < 3:
                    if (items.get(board[i+row_offset][j+column_offset]) != None) and (board[i+row_offset][j+column_offset] != '.'):
                        return False
                    items.update({board[i+row_offset][j+column_offset]:0})
                    j+=1
                i+=1
            column_offset+=3
            #print (items.keys()) #By here I have a full 3x3 done.
        row_offset+=3

    #Check that each row is unique:
    i = 0
    j = 0
    while i < 9:
        items = {}
        while j < 9:
            if items.get(board[i][j]) != None and board[i][j] != '.':
                return False
            items.update({board[i][j]:0})
            j+=1
        i+=1
        j=0

    i = 0
    j = 0
    while j < 9:
        items = {}
        while i < 9:
            if items.get(board[i][j]) != None and board[i][j] != '.':
                return False
            items.update({board[i][j]:0})
            i+=1
        j+=1
        i=0

    return True
#True
board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]


#False
board2 = [["8","1","3",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
# if(valid_sudoku(board2)):
#     print("TRUE")
# else:
#     print("FALSE")


#128
#Find the length of the longest consecutive element sequence in O(n) time.
#Obvious solution: Iterate over the array, and find the smallest element.
#Then do that again and see if the next smallest elements form a sequence or not.
#Problem: This is O(n^2) since each lookup is o(n) and we need to do n lookups.

#SOLUTION: If we use a HASHMAP when doing this, we get constant lookup times.
#This means we can now iterate through all elements (O(n)) and check if a sequence exists (O(1) for each lookup)
def longestConsecutive(nums):
    #Construct a dictionary representation of the array with dummy values (O(n).
    actual_longest=0
    nums_dict = dict.fromkeys(nums, 0)
    #By iterating over the array instead of the dictionary, we can pop from the dictionary which will eliminate duplicate lookups.
    for num in nums: 
        longest = 1
        num_up = num+1
        num_down = num-1
        while nums_dict.get(num_up) != None:
            nums_dict.pop(num_up)
            longest+=1
            num_up+=1
        while nums_dict.get(num_down) != None:
            nums_dict.pop(num_down)
            longest+=1
            num_down+=-1
        actual_longest = max(longest,actual_longest)
    return actual_longest

print(longestConsecutive([100,4,200,1,3,2]))

#It's too slow! Ok... Let's remove the dict item once it's counted.


