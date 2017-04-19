class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        index = 0
        tmp = None
        for i in range(len(nums)):
            if nums[i] != tmp:
                tmp = nums[i]
                nums[index] = tmp
                index += 1
        return len(nums[:index])