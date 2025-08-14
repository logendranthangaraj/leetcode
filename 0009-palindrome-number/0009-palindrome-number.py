class Solution(object):
    def isPalindrome(self, x):
        x = str(x)
        if str(x) == str(x[::-1]):
            return True
        else:
            return False