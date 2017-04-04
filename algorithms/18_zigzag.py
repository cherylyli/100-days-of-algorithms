class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        
        """
        if len(s) <= numRows or numRows == 1:
            return s

        rows = [[] for r in range(numRows)]
        s = list(s)
        ind_count = numRows-1
        
        # add each letter to a level
        for ind, c in enumerate(s):
            # figure out which row to append c to
            if ind_count + numRows-1 < ind:
                ind_count += (numRows - 2) * 2 + 2
            
            row_num = numRows-1 -  int(math.fabs(ind_count - ind))

            rows[row_num].append(c)

            
        # concat results
        rows = ["".join(r) for r in rows]
        return "".join(rows)

            
                
            
            