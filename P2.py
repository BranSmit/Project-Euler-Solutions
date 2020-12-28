# Even Fibonacci numbers

# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

fib = [1,2]
point = 1
n3 = 0

while n3 < 4000000:
    n0 = fib[point - 1]
    n1 = fib[point]
    n3 = n0 + n1
    fib.append(n3)
    point += 1

eFib = [s for s in fib if s % 2 == 0]
eFibSum = sum(eFib)

print (eFibSum)

# Solution: 4613732
