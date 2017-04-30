class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        intmax = 2 ** 31 - 1
        intmin = -(2 ** 31)
        int0 = ord('0')
        sign = 1
        str = str.strip()
        if str == '':
            return 0
        if str[0] == '-' or str[0] == '+':
            sign = -1 if str[0] == '-' else 1
            str = str[1:]
        result = 0
        for num in str:
            if '0' <= num <= '9':
                result = (ord(num) - int0) + result * 10
                if result > intmax:
                    return intmax if sign == 1 else intmin
            else:
                return result * sign
        return result * sign


a = Solution()
print(a.myAtoi('-2323232323123'))
