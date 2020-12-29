# 10001st prime

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?

def nthPrime(n):
    primes = []
    i = 0
    newi = 0
    u = 1
    while len(primes) > n:
        y = i/u
        if int(y) == y:
            u += 1
            
        
        
        
        i += 1

