class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if (s is None and t is None) or (len(s) == 0 and len(t) == 0 ):
            return True
        
        if s is None or t is None or len(s) == 0 or len(t) == 0 :
            return False
        
        mappingStoT = {}
        mappingTtoS = {}
        for i in range(0, len(s)):
            if s[i] in mappingStoT and t[i] != mappingStoT[s[i]]:
                return False
            
            if s[i] not in mappingStoT and t[i] in mappingTtoS:
                return False
                
            mappingStoT[s[i]] = t[i]
            mappingTtoS[t[i]] = s[i]
            
        return True