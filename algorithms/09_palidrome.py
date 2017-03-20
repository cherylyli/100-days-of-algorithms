class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        import re, string 
        regex = re.compile('[^a-zA-Z0-9]')
        s = regex.sub('', s)
        if len(s) <= 1:
            return True
            
            
        s = s.lower()
        print(s)
        i = 0
        j = len(s) - 1
        while i <= j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
                
        return True
                