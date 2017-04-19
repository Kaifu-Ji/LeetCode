class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1
        for i in range(1,len(digits) + 1):
            tmp = digits[-i] + carry
            digits[-i] = tmp % 10
            carry = tmp / 10
        if carry == 1:
            digits.insert(0, 1)
        return digits

Solution().plusOne([1,0])
