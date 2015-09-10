class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        if len(s) == 0  :
            return True
            
        countS = dict()
        countT = dict()
        
        for ch in s:
            if ch in countS:
                countS[ch] = countS[ch] + 1
            else:
                countS[ch] = 1
        
        for ch in t:
            if ch in countT:
                countT[ch] = countT[ch] + 1
            else:
                countT[ch] = 1
          
        for key in countS:
            if key in countT:
                if countS[key] == countT[key]:
                    continue;
                else:
                    return False
            else:
                return False

        return True