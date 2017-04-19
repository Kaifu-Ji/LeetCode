class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = list()
        symbol_set = {'[','(','{'}
        close_symbol = {']':'[',')':'(','}':'{'}
        for item in s:
            if item in symbol_set:
                stack.append(item)
            elif item in close_symbol:
                if len(stack) == 0 or close_symbol[item] != stack.pop():
                    return False
        if len(stack) == 0:
            return True
        return False