# 192 ms - 15/15 test cases

class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.ds = {}
        self.ds_arr = []


    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.ds:
            return False
        self.ds[val] = len(self.ds_arr)
        self.ds_arr.append(val)

        return True
        

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.ds:
            # swap position of val and last
            last = self.ds_arr[-1]
            pos_removed = self.ds[val]
            self.ds[last] = pos_removed
            self.ds_arr[pos_removed]= last
            
            
            self.ds_arr.pop(-1)
            
            
            del self.ds[val]

            return True
        return False
        

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        from random import randint
        key = self.ds_arr[randint(0, len(self.ds_arr)-1)]
        return key
        
        
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()