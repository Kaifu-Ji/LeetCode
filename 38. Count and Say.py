class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return '1'
        a = '1'
        i = 1
        result = '1'
        while n > i:
            result = ''
            tmp = a[0]
            count = 1
            for c in a[1:]:
                if c == tmp:
                    count += 1
                else:
                    result += str(count) + tmp
                    tmp = c
                    count = 1
            result += str(count) + tmp
            a = result
            i += 1
        return result


a = Solution()
print(a.countAndSay(4))
