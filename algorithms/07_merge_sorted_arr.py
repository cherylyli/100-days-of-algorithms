class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            for i in range(n):
                nums1[i] = nums2[i]
            return
        if n == 0:
            return
            
        # 3 pointers, one at end of nums1, one at end of nums2, one at the end of the m+n array nums1
        merge_pointer = m+n-1
        nums1_pointer = m-1
        nums2_pointer = n-1
        
        while nums1_pointer >=0 and nums2_pointer >= 0:
            if nums1[nums1_pointer] > nums2[nums2_pointer]:
                nums1[merge_pointer] = nums1[nums1_pointer]
                nums1_pointer -= 1
            else:
                nums1[merge_pointer] = nums2[nums2_pointer]
                nums2_pointer -= 1
                
            merge_pointer -= 1
            
        if merge_pointer >= 0 and nums2_pointer >=0:
            while nums2_pointer >=0:
                nums1[merge_pointer] = nums2[nums2_pointer]
                merge_pointer -= 1
                nums2_pointer -= 1