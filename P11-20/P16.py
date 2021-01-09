# Power digit sum

# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

# What is the sum of the digits of the number 2^1000?


# This is trivial

def sumOfDigits(n):
    return sum([int(i) for i in str(n)])


# Driver Code
print(sumOfDigits(2**1000))

# Solution: 1366