'''
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.

For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.
'''
class Solution(object):
    def numCombs(self, seq):
        if len(seq) == 1:
            return 1

        if len(seq) == 2:
            if seq[0] >= 2 and seq[1] > 6:
                return 1
            else:
                return 2

        if self.numCombs(seq[:2]) == 2:
            count_endSingle, count_endDouble = 1, 1
        else:
            count_endSingle, count_endDouble = 1, 0
            
        for i in xrange(2, len(seq)): #seed for first two elements already
            temp = count_endSingle
            count_endSingle = temp + count_endDouble
            if seq[i] <= 6 or seq[i-1] < 2:
                count_endDouble = temp
            else:
                count_endDouble = 0
                
        return count_endSingle+count_endDouble
        
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s is None or len(s) < 1:
            return 0

        if len(s) == 1:
            if int(s) in xrange(1, 27):
                return 1
            else:
                return 0

        nums = [int(ch) for ch in s]

        # handle '0's
        if nums[0] == 0:
            return 0
        
        mutableSeqs = []
        newSeqStarted = False
        hasImmutable = False # except mutables,check whether there is anything immutable (>3)
        for i in xrange(len(nums)):
            curNum = nums[i]
            if newSeqStarted:
                newSeq = mutableSeqs[-1]
                if curNum in xrange(1,3):
                    newSeq.append(curNum)
                elif curNum >=3 :
                    newSeq.append(curNum)
                    newSeqStarted = False #end of current Seq
                else: # curNum == 0
                    if newSeq[-1] in xrange(1,3):
                        hasImmutable = True
                        del newSeq[-1]
                        if len(newSeq) == 0:
                            del mutableSeqs[-1]
                        newSeqStarted = False
                    else:
                        return 0
            else:
                if curNum in xrange(1, 3):
                    newSeq = [curNum]
                    mutableSeqs.append(newSeq)
                    newSeqStarted = True
                elif curNum >= 3:
                    hasImmutable = True
                else: # curNum == 0
                    return 0
        
        if len(mutableSeqs) == 0:
            if hasImmutable :
                return 1
            else:
                return 0
        
        result = 1
        for seq in mutableSeqs:
            result *= self.numCombs(seq)

        return result
