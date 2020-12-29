# 10001st prime

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?


primes = [2]
def isPrime(n):
    for prime in primes:
        if n % prime == 0:
            return False
    return True

def nthPrime(n): 
    i = 2
    while len(primes) < n:
        if isPrime(i) == True:
            primes.append(i)
            # print(len(primes))
        i += 1
    return primes[-1]

print(nthPrime(10001))

# Solution: 104743


