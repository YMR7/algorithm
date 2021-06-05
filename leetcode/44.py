class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        size_s = len(s)
        # 记录上一次和 * 匹配的位置
        last_s_inx = -1
        # 记录上一次 * 出现的位置
        last_p_inx = -1
        s += '&'
        p += '&'
        i = 0
        j = 0
        while i < size_s:
            if s[i] == p[j] or p[j] == '?':
                i += 1
                j += 1
            # 遇到*时，直接当作''处理，记录此次遇到*的两个坐标，当发生不匹配时候，
            # 回溯到此处，从i+1处开始重新匹配
            elif p[j] == '*':
                # 连续的 * 等同于一个
                while p[j] == '*':
                    last_p_inx = j
                    j += 1
                last_s_inx = i
            # 不匹配，回溯到上一次遇到*的两个坐标位置，从下一个位置开始重新匹配
            elif last_p_inx > -1:
                # * 匹配一个    字符
                j = last_p_inx + 1
                last_s_inx += 1
                i = last_s_inx
            else:
                return False
        # s 到达终点后，判断 j 有没有到达终点
        while p[j] == '*':
            j += 1
        return p[j] == s[i]
                
