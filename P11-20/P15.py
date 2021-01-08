# Lattice paths

# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.


# How many such routes are there through a 20×20 grid?

# How the fu-
import math
from scipy import special

# After doing some research in Combinatorics, this is aparently really simple.
# It has to do with the binomial coefficient
# I love learning new math like this. It maybe takes a little away from the problem solving aspect,
# But it more than makes up for it with the math that I'm learning.

def countNELatticePathsSquare(n):
    binomC = int(special.binom(2*n,n))
    return binomC

# Hopefully I'll find an excuse to learn recursion some other day :)

print(countNELatticePathsSquare(20))

# Solution: 137846528820