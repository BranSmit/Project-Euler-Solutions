# Sum square difference

# Find the difference between the sum of the squares of the first 
# one hundred natural numbers and the square of the sum.

def ssd(n):
    numSet = [(i+1) for i in range(n)]
    squareOfSum = sum(numSet)**2
    sumOfSquare = sum([i**2 for i in numSet])
    diff = squareOfSum - sumOfSquare
    return diff

print(ssd(100))

# Solution: 25164150    
