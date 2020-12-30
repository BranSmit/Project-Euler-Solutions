# Largest prime factor

# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?


def smallestBaseDivisor(i):
    base = 2
    while i % base != 0:
        base += 1
    return base

def largestPrimeFactor(i):
    primeFactors = []
    runningI = i
    sbd = 2

    while runningI != 1:
        sbd = smallestBaseDivisor(runningI)
        # print("sbd:", sbd)
        if sbd not in primeFactors:
            primeFactors.append(sbd)
        runningI /= sbd
    
    return max(primeFactors)

print(largestPrimeFactor(600851475143))

# Solution: 6857
