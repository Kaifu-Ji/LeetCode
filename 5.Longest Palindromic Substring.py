class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 2:
            return s
        sa = preProcess(s)
        RL = [0] * len(sa)
        MaxRight = 0
        pos = 0
        maxpos = 0
        MaxLen = 0
        for i in range(1, len(sa) - 1):
            if i < MaxRight:
                RL[i] = min(RL[2 * pos - i], MaxRight - i)
            else:
                RL[i] = 0
            while sa[i + RL[i] + 1] == sa[i - RL[i] - 1]:
                RL[i] += 1
            if RL[i] + i > MaxRight:
                MaxRight = RL[i] + i
                pos = i
            if MaxLen < RL[i]:
                MaxLen = RL[i]
                maxpos = i
        start = int(((maxpos - MaxLen + 1) - 2) / 2)
        return s[start:start + MaxLen]


def preProcess(str):
    if len(str) == 0:
        return "^$"
    result = "^#"
    for char in str:
        result += char + '#'
    result += '$'
    return result


a = Solution()
print(a.longestPalindrome("babad"))
