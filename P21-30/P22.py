# Names scores

# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. 
# Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

# For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. 
# So, COLIN would obtain a score of 938 × 53 = 49714.

# What is the total of all the name scores in the file?

import string

# Extract data from file
fileObject = open("p022_names.txt", "r")
rawData = fileObject.read()
fileObject.close()

# Cleaning up data for maximum ease
nameData = [i.strip('"') for i in rawData.split(",")]
nameData.sort()

# Generating a dictionary of the letters of the alphabet and making them correspond to their alphabetical position
di = dict(zip(string.ascii_letters,[ord(c)%32 for c in string.ascii_letters]))
# print(di)

# Function for finding name score 
def findNameScore(name):
    value = sum([di[letter] for letter in name])
    position = nameData.index(name) + 1
    nameScore = value * position
    return(nameScore)

# Master function
def findTotalNS(nameList):
    total = 0
    for name in nameList:
        total += findNameScore(name)
    return total

# Driver code

solution = findTotalNS(nameData)
print(solution)

# Solution = 871198282




    