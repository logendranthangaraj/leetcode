class Solution(object):
    def romanToInt(self, s):
        romantoint = { 'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        res = 0;
        for i in range(len(s)):
            if i+1 < len(s) and romantoint[s[i]] < romantoint[s[i+1]]:
                res -= romantoint[s[i]]
            else:
                res += romantoint[s[i]]
        return res
