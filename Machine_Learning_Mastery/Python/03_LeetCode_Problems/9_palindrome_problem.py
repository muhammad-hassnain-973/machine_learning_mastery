# Mathemetical method 16ms time
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0 or (x%10==0 and x!=0) :
            return False
        reversed=0
        orignal=x
        while x>0:
            digit=x%10
            reversed=(reversed*10)+digit
            x//=10
        return orignal==reversed

# String method 2ms time
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0 or (x%10==0 and x!=0) :
            return False
        x=str(x)
        return x==x[::-1]