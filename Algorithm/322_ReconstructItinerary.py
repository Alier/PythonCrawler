'''
Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.

Note:
If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
All airports are represented by three capital letters (IATA code).
You may assume all tickets form at least one valid itinerary.
Example 1:
tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Return ["JFK", "MUC", "LHR", "SFO", "SJC"].
Example 2:
tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Return ["JFK","ATL","JFK","SFO","ATL","SFO"].
Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"]. But it is larger in lexical order.
'''

SRC = 0
DST = 1

class Solution(object):
    def findItineraryWithDepart(self, tickets, departure):
        #print tickets
        #print departure
        
        possibleDST =[]  # [(DST1,idx1),(DST2, idx2)..]
        for i in xrange(len(tickets)):
            if tickets[i][SRC] == departure:
                possibleDST.append((tickets[i][DST], i))
                
        if len(possibleDST) == 0:
            return [departure]
        
        possibleDST = sorted(possibleDST)
        for dst, i in possibleDST:
            #print (dst, i)
            itineraryAfter = self.findItineraryWithDepart(
                     tickets[:i]+tickets[i+1:],tickets[i][DST])
            #print itineraryAfter
            if len(itineraryAfter) == len(tickets):
                break

        result = [departure] + itineraryAfter 
        return result
                                               
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        return self.findItineraryWithDepart(tickets, "JFK")

st = Solution()
tickets = [["JFK", "MUC"],["NRT","JFK"],["JFK", "NRT"]]
print tickets
print st.findItinerary(tickets)
