# Special Pythagorean triplet

# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
import math

def isPT(triple):
    if triple[0]**2 + triple[1]**2 == triple[2]**2:
        return True
    else:
        return False

# Euclids Formula Baby!
# Where m > n > 0:
# a = m^2 - n^2, b = 2mn, c = m^2 + n^2

m = 2                                   # I know it's dirty, but it works and I dont feel like refactoring
n = 1
a,b,c = 0,0,0
q = False
while True:
    if q == True:
        break
    for _ in range(500):
        if q == True:
            break
        m += 1
        n = 1
        for u in range(m):
            n += 1
            a = (m**2) - (n**2)
            b = 2*m*n
            c = (m**2) + (n**2)
            if a + b + c == 1000:
                print(a,b,c)
                print(isPT([a,b,c]))
                print(a * b * c)
                q = True
                break

# Solution: 31875000





