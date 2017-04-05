class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_dict = {}
        start = max_length = 0
        for i in range(len(s)):
            char = s[i]
            if char in char_dict and start <= char_dict[char]:
                start = char_dict[s[i]] + 1
            else:
                max_length = max(max_length, i - start + 1)
            char_dict[char] = i
        return max_length
