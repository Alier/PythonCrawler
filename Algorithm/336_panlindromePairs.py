'''
Given a list of unique words. Find all pairs of distinct indices (i, j) in the given list, so that the concatenation of the two words, i.e. words[i] + words[j] is a palindrome.

Example 1:
Given words = ["bat", "tab", "cat"]
Return [[0, 1], [1, 0]]
The palindromes are ["battab", "tabbat"]
Example 2:
Given words = ["abcd", "dcba", "lls", "s", "sssll"]
Return [[0, 1], [1, 0], [3, 2], [2, 4]]
The palindromes are ["dcbaabcd", "abcddcba", "slls", "llssssll"]
'''
ORIG_MARK=0
REV_MARK=1

WORD = 0
MARK = 1
IDX = 2

EMPTY_STR = ""

class Solution(object):
    def isPalindrome(self, word):
        return word == word[::-1]
        
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        if words is None or len(words) < 2:
            return []

        result = []
        # edge case, empty str "" would work with all other strings
        emptyStrIdxs = [i for i in xrange(len(words)) if words[i] == ""]
        if len(emptyStrIdxs) > 0:
            for m in xrange(len(emptyStrIdxs)):
                i = emptyStrIdxs[m]
                result += [[i, idx] for idx in emptyStrIdxs[m+1:]]
                result += [[idx, i] for idx in emptyStrIdxs[m+1:]]
                
        newwords = []
        for i in xrange(len(words)):
            if i not in emptyStrIdxs:
                word = words[i]
                newwords.append((word, ORIG_MARK, i))
                newwords.append((word[::-1], REV_MARK, i))

        newwords = sorted(newwords)
        print newwords
        firstDistinctWords = dict()
        count = 0
        #print newwords
        for i in xrange(len(newwords)-1):
            print "====== i: %d, curWord= %r" % (i, newwords[i])
            print firstDistinctWords
            print result

            curWord, curMark, curIdx = newwords[i]
            # already have same word counted before
            # THIS IS ONLY useful improvement if there is a lot of repeat string in test set. 
            if curMark == 0 and curWord in firstDistinctWords:
                print "here 1"
                preIdx = firstDistinctWords[curWord]
                curIdx = curIdx
                samePairs1 = [[curIdx, y] for [x, y] in result if x == preIdx and y != curIdx]
                samePairs2 = [[x, curIdx] for [x, y] in result if y == preIdx and x != curIdx]
                result = result + samePairs1 + samePairs2
                if [preIdx, curIdx] in result:
                    result.append([curIdx, preIdx])
                elif [curIdx, preIdx] in result:
                    result.append([preIdx, curIdx])
                print result
                print "shortcut!"
                continue

            # self is palindrome, could be coupled with all emptyStr
            if len(emptyStrIdxs) > 0 and curMark == 0 and self.isPalindrome(curWord):
                print "here2"
                result += [[idx, curIdx] for idx in emptyStrIdxs]
                result += [[curIdx, idx] for idx in emptyStrIdxs]
                print result
                #firstDistinctWords[curWord] = curIdx
                
            j = i+1
            # don't compare with its own reverse
            # compare with all with differnt idx , different MARK and same start char
            while j < len(newwords) and \
                   curWord == newwords[j][WORD][:len(curWord)]:
                count += 1
                newWord, newMark, newIdx = newwords[j]
                if (curIdx != newIdx and curMark != newMark):
                    if len(curWord) == len(newWord) or self.isPalindrome(newWord[len(curWord):]):
                        if curMark == 0: 
                            firstDistinctWords[curWord] = curIdx
                            result.append([curIdx,newIdx])
                        else: # newMark == 0
                            #firstDistinctWords[newWord] = newIdx
                            result.append([newIdx,curIdx])
                            
                j += 1
                        
        print count
        return result 
