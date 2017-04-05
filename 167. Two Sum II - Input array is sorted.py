class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        lo = 0
        hi = len(numbers) - 1
        current_num = numbers[lo] + numbers[hi]
        while current_num!= target:
            if current_num:
                if current_num > target:
                    hi -= 1
                else:
                    lo += 1
        return [lo + 1,hi + 1]

s = Solution()
s.twoSum()