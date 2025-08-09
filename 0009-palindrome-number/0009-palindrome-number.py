class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # Negative numbers or numbers ending in 0 (but not 0 itself) are not palindrome
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10
        
        # For odd number of digits, drop the middle digit from reversed_half
        return x == reversed_half or x == reversed_half // 10