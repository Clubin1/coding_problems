class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        """
        init dictionary
        for i in range of nums
            currnum = nums[i]
            diff = target - currnum
            
            if diff in dictionary and currnum != i 
                return [list[diff], i]
            else
                list[currNum] = i
        """
        list = {}
        
        for i in range(len(nums)):
            currNum = nums[i]
            difference = target - currNum

            if difference in list and currNum != i:
                return[list[difference], i]

            else:
                list[currNum] = i
    print(twoSum(object,[2,1,9,4,4,56,90,3], 8))