import sys

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if s is None or numRows == 0:
            return None
        
        if numRows == 1 or s == '':
            return s
        
        rows = [[] for i in xrange(numRows)]
        idx = 0
        forward = True
        for ch in s:
            rows[idx].append(ch)
            if forward:
                if idx == numRows-1:
                   forward = False
            else:
                if idx == 0:
                   forward = True

            if forward:
                idx += 1
            else:
                idx -= 1

        print rows        
        result=''
        for row in rows:
            result += ''.join(row)

        return result

if __name__ == '__main__':
    st = Solution()
    if sys.argv[1] is not None and sys.argv[2] is not None:
        print 'Calculate zipzag for string '+sys.argv[1]+"with rows="+sys.argv[2]
        print st.convert(sys.argv[1],int(sys.argv[2]))
    
