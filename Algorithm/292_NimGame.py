# solution is based on conclusion: if after your move, opponent has 4n stones left then you can always win.  That means, when it's your turn, as long as the stone counts between 5 - 7 (by which you remove 1 - 3 stone would result in 4 for next person), you will always win.
class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return (n-1)%4 == 0 or (n-2)%4 == 0 or (n-3)%4 == 0