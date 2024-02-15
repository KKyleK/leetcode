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