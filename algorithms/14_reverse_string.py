class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) <= 1:
            return s
        
        #iteratively
        s = list(s)
        i = 0
        j = len(s)-1
        while i < j:
            #swap s[i] and s[j]
            temp = s[i]
            s[i] = s[j]
            s[j] = temp
            j -= 1
            i += 1
        return "".join(s)