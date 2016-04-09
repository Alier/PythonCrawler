'''Compare two version numbers version1 and version2.
    If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.
'''
import string
import sys

class Solution(object):
    def equalToZero(self, vtail):
	    if all(int(x) == 0 for x in vtail):
	        return True
	    return False
		
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        if version1 is None or version2 is None:
            return 0
        
        # remove all spaces in the string, head, tail and inbetween numbers
        version1 = string.join(version1.strip().split(' '),'')
        version2 = string.join(version2.strip().split(' '),'')
        
        v1s = version1.split('.')
        v2s = version2.split('.')

        for i in xrange(0, min(len(v1s), len(v2s))):
            v1, v2 = map(int, (v1s[i], v2s[i]))
        
            if v1 < v2:
                return -1
            elif v1 > v2:
                return 1
            else: # v1 == v2
                if i < min(len(v1s), len(v2s)) - 1: 
                    continue
                else: # last element for one of the version string
                    if self.equalToZero(v1s[i+1:]) and self.equalToZero(v2s[i+1:]):
                        return 0
                    if self.equalToZero(v1s[i+1:]) and not self.equalToZero(v2s[i+1:]):
                        return -1
                    else: 
                        return 1

if __name__ == '__main__':
    st = Solution()
    print st.compareVersion(sys.argv[1], sys.argv[2])
    
