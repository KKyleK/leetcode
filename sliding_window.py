#121: Best time to Buy and Sell Stock
# idea:
# For each price, if it's lower, make that the new start.
# If it's higher, calculate the profit and save it. Done.
def maxProfit(prices):
    start = prices[0]
    maxProfit = 0
    for p in prices:
        if p > start:
            profit = p-start
            if profit > maxProfit:
                maxProfit = profit
        elif p < start:
            start = p
    return maxProfit

# print(maxProfit([4,1,5,2,7]))

#3: Longest Substring Without Repeating Characters
# Idea: Record elements of the string until we hit a duplicate. When a duplicate is hit,
# save the length of the current string.
# Remove elements of the string until the original is removed, then add the duplicate and continue.
def lengthOfLongestSubstring(s):
    currentString=""
    longestSubstring = 0

    index = 0
    while index < len(s):
        #The letter is already in the string, save, then pop until the duplicate is gone, and add the new one in.
        if s[index] in currentString:
            currentLength = len(currentString)
            if currentLength > longestSubstring:
                longestSubstring = currentLength

            remove = currentString[0]
            currentString = currentString[1:]
            while remove is not s[index]:
                remove = currentString[0]
                currentString = currentString[1:]

        currentString+=s[index]
        index+=1
    #Check if the resulting string is the longest substring.
    currentLength = len(currentString)
    if currentLength > longestSubstring:
        longestSubstring = currentLength

    return longestSubstring

# print(lengthOfLongestSubstring(""))

#424: Longest repeating character replacement.
# Goal: Form the longest line of repeating characters.
#
# Idea: Maintain a list of characters. As long as the list has k+1 unique characters or less, keep adding.
# Once we get > k+1 unique characters, save the length, add the new character, and pop until we are back to k+1 unique characters.

def characterReplacement(s, k):
    currentString =""
    longestSubstring = 0
    replacements = 0
    index = 0
    while index < len(s):
        #See if we need to use a replacement.
        if (len(currentString) > 0) and (s[index] != currentString[0]):
            replacements+=1
            #Too many unique characters, save what we have.
            if replacements > k:
                #print(currentString)
                if len(currentString) > longestSubstring:
                    longestSubstring = len(currentString)
                #Pop off the unique characters at the beginning.
                toRemove = currentString[0]
                toRemoveIndex=1
                while toRemoveIndex < len(currentString):
                    if currentString[toRemoveIndex] == toRemove:
                        toRemoveIndex+=1
                    else:
                        break
                # print("before removal")
                # print(currentString)
                currentString = currentString[toRemoveIndex:]
                # print("after removal")
                # print(currentString)
                # #Have to recompute number of replacements.
                # replacements=0
                # counter = 1
                # replaceTo = currentString[0]
                # while counter < len(currentString):
                #     if currentString[counter] != replaceTo:
                #         replacements+=1
                #     counter+=1
                # print(replacements)


        currentString+=s[index]

        #recompute number of replacements.
        replacements=0
        counter = 1
        replaceTo = currentString[0]
        while counter < len(currentString):
            if currentString[counter] != replaceTo:
                replacements+=1
            counter+=1


        index+=1

    if len(currentString) > longestSubstring:
        longestSubstring =len(currentString)
    return longestSubstring

print(characterReplacement("AABABBA", k = 1))
# print(characterReplacement("ABAB", k = 2))

print(characterReplacement("abccdefghhababa",2))
# #should be 3.
print(characterReplacement("AAAB",0))

print(characterReplacement("AABABBA", k = 0))



#FAIL! Should be 4:
print(characterReplacement("ABBB",2))
#lol...Yeah... this certainly beats what I was thinking of looking at the first letter in the sequence...


#Ok, mistake: need to keep track of uniqueCharacters IN ORDER. AABAA represents 3 unique characters.
#
#
#Error in my thought process: if we look at the last digit in a sequence to determine if a unique should be added, we screw up!
#Example:
#
# "AAB"   next is A.   We shouldn't add a unique here because 'A' is already in the sequence. But B is next. DON'T Add unique!
#
# Old method was correct. it was NOT correct to do IN ORDER!!! AABAA is 2 UNIQUE characters!!! BUT AABAABAA can't be used...
#
#Need a new way of determining if it's unique... probably turn the letter into an A?
# Testing:
#
#IDEA: do the replacements. When out of replacements, remove.
#
# AABAA -> AAAAA (replace)
# AAAAAC -> C (out of replacements, delete uniques in a row.)
#
#
# AAA
# AAAB -> no replacements. Delete.
#
# ABAB:
# A
# AA (replace)
# AAA
# AAAA (replace) ok.
#
#
#
# turns out this doesn't work either. Deleting becomes impossible, because if aaab and aaa is deleted, how many replacements are given back?
# 1? 2? Impossible to tell.
#
# Summary of attempts:
# 1. Use a replacement when something encountered is different than the last character:
#    aabaa -> gets treated as 3 replacements. Wrong.
# 2. Use a replacement when a non unique character is encountered:
#    aabbaabbaa...  -> is only 2 even though it should be 4.
# 3. Use a replacement when something encountered is different than the last character:
#    aaaab -> when removing, we don't know how many replacements to get back.
#
# SOLUTION: use (3) but with a modification: we keep track of the letter we are trying to replace for, BUT on removing,
# we use the actual string.
# In other words, use a replacement when something encountered is different than the FIRST character.
#
# -> need to recompute number of replacements... otherwise: abccd goes:
# abc
# bcc
# ccd (the second c is treated as a replacement)
#
#
# ABBB fails epicly... Looking at the last character has to be the correct idea, but i'll drop this for now. Probably over complicated it.
# Hint is don't "shrink" the window, just glide it.

