'''
Given an array of strings, group anagrams together.

For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"], 
Return:

[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:
For the return value, each inner list's elements must follow the lexicographic order.
All inputs will be in lower-case.
'''
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if strs is None or len(strs) <= 1:
            return [strs]

        wordsByLength = dict()
        for word in strs:
            if str(len(word)) in wordsByLength:
                wordsByLength[str(len(word))].append(word)
            else:
                wordsByLength[str(len(word))] = [word]
        
        print wordsByLength
        groupsByKey = dict()
        for wordlen, words in wordsByLength.items():
            for w in words:
                key = ''.join(sorted(w))
                if len(groupsByKey) == 0 or key not in groupsByKey:
                    groupsByKey[key] = [w]
                else:
                    groupsByKey[key].append(w)

        print groupsByKey
        return [sorted(g) for (k,g) in groupsByKey.items()]
