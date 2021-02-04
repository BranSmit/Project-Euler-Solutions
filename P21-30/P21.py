# Amicable numbers

# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

# Evaluate the sum of all the amicable numbers under 10000.

import math as mt

def AmicableSum(num):
    def d(n):
        PDSum = 0
        for i in range(int(n/1.9)):
            if i > 0 and n % i == 0:
                PDSum += i
        return PDSum

    amics = []
    for i in range(num):
        s1 = d(i)
        for j in range(i):
            s2 = d(s1)
            if s2 == i:
                if s1 not in amics:
                    amics.append(s1)
                if i not in amics:
                    amics.append(i)
                    
        if i % 10 == 0:
            print(i)
                    
    return sum(amics)

# print(AmicableSum(10000))
                
        
N = 100005
  
# Function to return all amicable numbers 
def AMICABLE(): 
  
    Sum = [0 for i in range(N)] 
      
    for i in range(1, N): 
        Sum[i] += 1
  
        for j in range(2, mt.ceil(mt.sqrt(i))):  
  
            # j is proper divisor of i 
            if (i % j == 0): 
                Sum[i] += j 
  
                # if i is not a perfect square 
                if (i // j != j): 
                    Sum[i] += i // j 
  
    s = set() 
    for i in range(2, N): 
        if(i != Sum[i] and Sum[i] < N and 
           i == Sum[Sum[i]] and i not in s and 
                Sum[i] not in s): 
            s.add(i) 
            s.add(Sum[i]) 
  
    return s 
  
# function to findSum of all amicable  
# numbers up to N 
def SumOfAmicable(n): 
  
    # to store requiredSum 
    Sum = 0
  
    # to store all amicable numbers 
    s = AMICABLE() 
  
    #Sum all amicable numbers upto N 
    s = sorted(s) 
    for i in s: 
        if (i <= n): 
            Sum += i 
        else: 
            break
      
    # required answer 
    return Sum
  
# Driver Code 
n = 10000
print(SumOfAmicable(n)) 
  
# This code is contributed by  
# mohit kumar 29 

