def twoSum( nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        indList = []
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] + nums[j] == target:
                    indList =   [i,j]
                    return indList
            
print(twoSum([3,2,4],6))