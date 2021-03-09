# Non-abundant sums

# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. 
# For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. 
# By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. 
# However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed 
# as the sum of two abundant numbers is less than this limit.

# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
import math

def sievePrimes(n):
    bucket = [i+2 for i in range(n-1)]
    i = 0
    cp = 0
    # print(bucket)
    while True:
        cp = bucket[i]
        try:
            while True:
                i += cp
                bucket[i] = 0
        except:
            i = cp-1
        try:
            while bucket[i] == 0:
                    i += 1
        except:
            filBuck = []
            for u in bucket:
                if u != 0:
                    filBuck.append(u)
            return filBuck  
        
def primeFactorization(n):
    primesUnderN = sievePrimes(n)
    flag = False
    sucPrimes = {}
    i = 0
    while flag == False and i < len(primesUnderN):
        if n % primesUnderN[i] == 0:
            n /= primesUnderN[i]
            if primesUnderN[i] not in sucPrimes:
                sucPrimes[primesUnderN[i]] = 0
            sucPrimes[primesUnderN[i]] += 1 
        else:
            i += 1
    return sucPrimes

# Sum of Divisors Function
def S(n): 
    pf = primeFactorization(n)
    # print (pf)
    sums = [] 
    for key in pf:
        power = pf[key]
        runningSum = 0
        for p in range(power + 1):
            subtotal = key ** p
            # print(key, p, subtotal)
            runningSum += subtotal
        sums.append(runningSum)
    return math.prod(sums)
   

def isAbundant(n):
    if S(n) > n:
        return True
    else:
        return False

def nonAbundantSum():
    for n in 

print(nonAbundantSum())