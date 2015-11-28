class Solution(object):
	def findAscendingSubset(self, nums):
		# this function finds all longest subsets ascending in nums.
		# e.g.for [0,3,6,1,4] , should return [[0,3,6],[0,3,4],[0,1,4]]
		if len(nums) == 1:
			return [nums]
	
		curNum = nums[0]	
		subSetsFromNext = self.findAscendingSubset(nums[1:])
		notLargest = False
		result = []
		notLargest = False
		for subset in subSetsFromNext:
			if curNum < subset[0]:
				newSubset = list(subset)
				newSubset.insert(0,curNum)
				result.append(newSubset)
				notLargest = True
				if curNum+1 < subset[0]: #more than distance 1
					result.append(subset)
			else:
				result.append(subset)
		
		if notLargest is False:
			result = result+[[curNum]]		
		
		return result
		
			
	def minDistance(self, word1, word2):
		"""
		:type word1: str
		:type word2: str
		:rtype: int
		"""
		result = 0
		shortWord = word1
		longWord = word2
				
		if len(word1) > len(word2):
			longWord = word1
			shortWord = word2

		print "short="+shortWord
		print "long="+longWord
		if len(shortWord) == 0:
			return len(longWord)
			
		indexShortToLong = {}
		indexLongToShort = {}
		shortWordIndex = []
		longWordIndex = [] # [[]]
		
		for i in range(0,len(shortWord)):
			for j in range(0, len(longWord)):
				if longWord[j] == shortWord[i]:
					indexLongToShort[j] = i
					if i in indexShortToLong:
						indexShortToLong[i].append(j)
					else:
						indexShortToLong[i] = [j]
						shortWordIndex.append(i)
									
		print "indexShortToLong"
		print indexShortToLong	
		print "indexLongToShort"
		print indexLongToShort		
		print "shortWordIndex"
		print shortWordIndex
		
		longWordIndex.append([])
		for i in shortWordIndex:
			curElemIndexInLong = indexShortToLong[i]
			if len(curElemIndexInLong) > 1: # more than one location found in longWord
				curLongWordIndex = list()
				for item in longWordIndex:
					curLongWordIndex.append(list(item))
					
				#add the first index to current indexLists
				for item in longWordIndex:
					item.append(curElemIndexInLong[0])
				startIndex = 0
				for i in range(1, len(curElemIndexInLong)):
					startIndex += len(curLongWordIndex)
					for item in curLongWordIndex:
						longWordIndex.append(list(item))
					for j in range(startIndex, len(longWordIndex)):
						longWordIndex[j].append(curElemIndexInLong[i])
			else:
				for item in longWordIndex:
					item.append(curElemIndexInLong[0])
					
		print "longWordIndex"
		print longWordIndex
	
		if len(longWordIndex) == 0: # no duplicate 
			return len(longWord)
		
		if len(shortWordIndex) == len(longWordIndex) : # nothing needs to change
			return 0
			
		if len(shortWordIndex) == 1:
			#print "coming here:"
			elementBefore = shortWordIndex[0]
			elementAfter = len(shortWord) - 1 - shortWordIndex[0] 
			#print elementBefore
			#print elementAfter
			if longWordIndex[0] > elementBefore:
				elementBefore = longWordIndex[0]
			if len(longWord) - longWordIndex[0] > elementAfter:
				elementAfter = len(longWord) -1 - longWordIndex[0]
			print elementBefore
			print elementAfter
			
			return elementBefore + elementAfter
		
		#find the longest ascending subsets of longWord
		longWordSubsetAll = []
		for seq in longWordIndex:
			seqsForCurElem = self.findAscendingSubset(seq)
			for item in seqsForCurElem:
				longWordSubsetAll.append(item)
				
		print "longWordSubsetAll"
		print longWordSubsetAll
		
		LongestLen = len(longWordSubsetAll[0])
		longestWordSubsetAll = [longWordSubsetAll[0]]
		for i in range(1, len(longWordSubsetAll)):
			if len(longWordSubsetAll[i]) > LongestLen:
				LongestLen = len(longWordSubsetAll)
				longestWordSubsetAll = []
				longestWordSubsetAll.append(longWordSubsetAll[i])
			elif len(longWordSubsetAll[i]) == LongestLen:
				longestWordSubsetAll.append(longWordSubsetAll[i])
		
		print "longestWordSubsetAll"
		print longestWordSubsetAll
		
		return 0
				
		shortWordSubset = []
		i = 0 
		startIndex = i+1
		while i < len(longWordIndex)-1:
			longWordSubset.append([longWordIndex[i]])
			shortWordSubset.append([shortWordIndex[i]])
			currentHighIndex = longWordIndex[i]
			for j in range(startIndex, len(longWordIndex)):
				if longWordIndex[j] >= currentHighIndex:
					currentHighIndex = longWordIndex[j]
					longWordSubset[i].append(longWordIndex[j])
					shortWordSubset[i].append(shortWordIndex[j])
				else:
					break;
			if j == len(longWordIndex)-1:
				i += 1
			else:
				
				startIndex = j+1
		
		print "long:"
		print longWordSubset
		print shortWordSubset
		longestSubsetLong = longWordSubset[0]
		smallestStartDiff = abs(longWordSubset[0][0] - shortWordSubset[0][0])
		longestSubsetShort = shortWordSubset[0]
		
		for i in range(1, len(longWordSubset)):
			if len(longWordSubset[i]) >= len(longestSubsetLong) and abs(longWordSubset[i][0] - shortWordSubset[i][0]) < smallestStartDiff:
				longestSubsetLong = longWordSubset[i]
				longestSubsetShort = shortWordSubset[i]
				smallestStartDiff = abs(longWordSubset[i][0] - shortWordSubset[i][0])
				
		print "longest"
		print longestSubsetLong
		print longestSubsetShort
		
		elementBefore = longestSubsetShort[0]
		elementAfter = len(shortWord) - 1 - longestSubsetShort[-1]
		elementInBetween = longestSubsetShort[-1] - (longestSubsetShort[0]+1)
		existElementInBetween = len(longestSubsetLong) - 2
		if longestSubsetLong[0] > elementBefore:
			elementBefore = longestSubsetLong[0]
		
		if len(longWord) - 1 - longestSubsetLong[-1] > elementAfter:
			elementAfter = len(longWord) - 1 - longestSubsetLong[-1]
			
		if longestSubsetLong[-1] - (longestSubsetLong[0]+1) > elementInBetween:
			elementInBetween = longestSubsetLong[-1] - (longestSubsetLong[0]+1)
		
		print elementBefore
		print elementAfter
		print elementInBetween
		
		return elementBefore+elementAfter+(elementInBetween-existElementInBetween)
			
st = Solution()
#print st.findAscendingSubset([0,3,4,6,1,5])
print st.minDistance("industryrr","interest")