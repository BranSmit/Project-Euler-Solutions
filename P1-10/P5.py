# Smallest multiple


# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# Not gonna generalize this one because I dont really feel like it.

sm = 2520
numSet = [i+1 for i in range(20)]
while True:
    n=0
    for i in numSet:
        if sm % i != 0:
            sm += 20
            break
        else:
            n += 1
    if n == 20:
        break

print(sm,"\n")
for o in numSet:
    print(sm / o)
    
# Solution: 232792560 
