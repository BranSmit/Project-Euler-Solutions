# Number letter counts

# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) 
# contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

def numToWord4D(num):
    # First we split the number into it's base 10 places.
    splitNum = [int(n) for n in str(num)]
    for rep in (range(4-len(splitNum))):
        splitNum.insert(0,0)

    # Creating storage of weird numbers that will be called often
    b10WordBank = ('one','two','three','four','five','six','seven','eight','nine')
    teenWordBank = ('eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen')
    tensWordBank = ('ten','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety')

    # Now we set rules for the number in each place.
    ones  = ''
    thous = ('',b10WordBank[splitNum[0]-1]+' thousand ')[splitNum[0] > 0]
    hunds = ('',b10WordBank[splitNum[1]-1]+' hundred ')[splitNum[1] > 0]
    ones = ('',b10WordBank[splitNum[3]-1])[splitNum[3] > 0]
    
    # Handling tens place last to deal with 'teen' exeptions
    if splitNum[2] ==  1 and splitNum[3] > 0:
        tens = teenWordBank[splitNum[3]-1]
        ones = ''
    else:
        tens = ('', tensWordBank[splitNum[2]-1]+' ')[splitNum[2]>0]
        
    # Test for 'and' according to the brits
    ifAnd = ('', 'and ')[num>100 and sum(splitNum[2:4])>0]
    
    # Connocate and return
    word = thous + hunds + ifAnd + tens + ones
    if len(word)>0:
        return word
    else:
        return 'zero'


# Driver Code
numRange = [i+1 for i in range(1000)]
totalChar = 0

for num in numRange:
    dword = numToWord4D(num)
    word = dword.replace(' ','')
    wordLen = len(word)
    totalChar += wordLen

print(totalChar)

# Solution: 21124
