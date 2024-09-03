class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        thisdict = {}
        for i in range(len(s)):
            thisdict[s[i]] = thisdict.get(s[i], 0) + 1
            thisdict[t[i]] = thisdict.get(t[i], 0) - 1
            
        for j in thisdict.values():
            if j != 0:
                return False
        return True
                