# Summation of primes

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

# God the Sieve of Eratosthenes is wonderful
def sumSievePrimes(n):
    bucket = [i+2 for i in range(n-1)]
    i = 0
    cp = 0
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
            return sum(bucket)

print(sumSievePrimes(2000000))



















# # EZPZ, just gotta modify my prime generator a bit.
# primes = [2]
# def isPrime(n):
#     for prime in primes:
#         if n % prime == 0:
#             return False
#     return True

# def sumOfPrimes(n): 
#     i = 3
#     for _ in range(int((n-1)/2)):
#         if isPrime(i) == True:
#             primes.append(i)
#             # print(len(primes))
#         i += 2
#         if _ % 1000 == 0:
#             print(_)
#     sop = sum(primes)
#     return sop

# print(sumOfPrimes(2000000))