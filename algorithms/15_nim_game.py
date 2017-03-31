class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        if n == 1:
            return True
            
        moves = [False, True, True]
        can_win = None
        for i in range(3, n+1):
            if moves[0] and moves[1] and moves[2]:
                moves.append(False)
            else:
                moves.append(True)
            moves = moves[1:]
            

        return moves[-1]
            