class Solution(object):
    def isPalindrome(self, x):
        readNumber = str(x)
        reverseNumber = str(x)[::-1]
        if reverseNumber == readNumber:
            return True
        else:
            return False

