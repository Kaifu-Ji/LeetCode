class Solution(object):
    @staticmethod
    def twoSum(nums, target):
        nums_dict = dict()
        for i in range(len(nums)):
            target_num = target - nums[i]
            if target_num in nums_dict:
                return [nums_dict[target_num], i]
            nums_dict[nums[i]] = i;

a = Solution()
print a.twoSum([2, 7, 11, 15],9)
