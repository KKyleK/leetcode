#13:Roman to integer

romanToInteger = {
            "I" : 1,
            "IV": 4,
            "V" : 5,
            "IX" : 9,
            "X" : 10,
            "XL" : 40,
            "L" : 50,
            "XC": 90,
            "C" : 100,
            "CD": 400,
            "D" : 500,
            "CM": 900,
            "M" : 1000
        }


def romanToInt(s):
        sum = 0
        counter = 0
        while counter < len(s):
            currentLetter = s[counter]
            if ((counter+1) < len(s)):
                if currentLetter == 'I':
                    if s[counter+1] == 'V':
                        sum+=romanToInteger["IV"]
                        counter+=2
                        continue
                    elif s[counter+1] == 'X':
                        sum+=romanToInteger["IX"]
                        counter+=2
                        continue
                elif currentLetter == 'X':
                    if s[counter+1] == 'L':
                        sum+=romanToInteger["XL"]
                        counter+=2
                        continue
                    elif s[counter+1] == 'C':
                        sum+=romanToInteger["XC"]
                        counter+=2
                        continue
                elif currentLetter == 'C':
                    if s[counter+1] == 'D':
                        sum+=romanToInteger["CD"]
                        counter+=2
                        continue
                    elif s[counter+1] == 'M':
                        sum+=romanToInteger["CM"]
                        counter+=2
                        continue
            sum+=romanToInteger[currentLetter]
            counter+=1
        return sum

#1994
# roman = "MCMXCIV"
# print(romanToInt(roman))

#12: Integer to Roman

#Reverse integerToRoman.
integerToRoman = {}
for key,value in romanToInteger.items():
    integerToRoman.update({value:key})

#Idea: Attempt to use the largest roman numeral to subtract from the num.
#Repeat until at 0.
#Since the largest number possible is 3999, it's impossible for us to use the same numeral 4 times in a row,
#so we don't need to worry about that.
def intToRoman(num):
    roman=""
    tryToSubtract = list(integerToRoman.keys())
    tryToSubtract.sort(reverse=True)
    print(tryToSubtract)

    counter=0
    while counter < len(tryToSubtract) and num != 0:
        if tryToSubtract[counter] <= num:
            num-= tryToSubtract[counter]
            roman+=integerToRoman[tryToSubtract[counter]]
        else:
            counter+=1
    return roman
print(intToRoman(1))