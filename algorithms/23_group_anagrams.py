# Needs improvement, too slow


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        def hashStr(s):
            """
            Given one string, give back a dict of letters that appeared and occurrences
            """
            s = list(s)
            hashed = {}
            num = 0
            for c in s:
                num += ord(c)
                if c in hashed:
                    hashed[c] += 1
                else:
                    hashed[c] = 1
            return hashed, num
                
        def compTwoHashes(hs1, hs2):
            """
            Given two dicts, return true if they're the same (by value)
            """
            for key1 in hs1:
                if key1 not in hs2:
                    return False
                    
            for key2 in hs2:
                if key2 not in hs1:
                    return False
                if hs1[key2] != hs2[key2]:
                    return False
            return True
            

            
            
        if len(strs) == 0 or len(strs) == 1:
            return [strs]
            
        # create list of anagrams
        # list of anagram dicts
        # list of anagram dicts mapped to same dict
        anagram_lists = []
        anagram_dicts = []
        anagram_dict_inds = {}
        
        
        
        for s in strs:
            hashed_str, key = hashStr(s)
            found_fam = False
            
            # for each key in hashed_str, find corresponding dict in anagram_dicts
            if key in anagram_dict_inds:
                for ind in anagram_dict_inds[key]:
                    if compTwoHashes(anagram_dicts[ind], hashed_str):
                        found_fam = True
                        anagram_lists[ind].append(s)
                        break
                if not found_fam:
                    anagram_dict_inds[key].append(len(anagram_dicts))
                    anagram_dicts.append(hashed_str)
                    anagram_lists.append([s])
                        
                    
            else: 
                anagram_dict_inds[key] = [len(anagram_dicts)]
                anagram_dicts.append(hashed_str)
                anagram_lists.append([s])
                
            # print(hashed_str)
            # print(anagram_dicts)

        return anagram_lists
        
        
        
        