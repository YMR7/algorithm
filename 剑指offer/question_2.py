class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        #  return s.replace(' ', '%20')
        s = list(s)
        size = len(s)
        for i in range(size):
            if s[i] == ' ':
                s[i] = '%20'
        return ''.join(s)
