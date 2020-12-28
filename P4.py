# Largest palindrome product

# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

def isPalindrome(num):
    antiNum = [i for i in str(num)]
    antiNum.reverse()
    antiNum = int("".join(antiNum))
    if num == antiNum:
        return True
    else:
        return False


def lpp(digits):
    # Generates the largest number with a given amount of digits
    n1 = (10**digits) - 1
    palList = []
    f1 = n1
    while f1 >= 10**(digits-1):
        f2 = n1
        while f2 >= 10**(digits-1):
            f3 = f1 * f2
            f2 -= 1
            if isPalindrome(f3) == True:
                palList.append(f3)
        f1 -= 1 
    return max(palList)

print(lpp(3))
        
# Solution: 906609