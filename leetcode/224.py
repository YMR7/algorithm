class Solution:
    def calculate(self, s: str) -> int:
        
        def helper(li):
            sign = '+'
            stack = []
            num = 0
            while li:
                ch = li.pop(0)
                if ch.isdigit():
                    # 连续多个数字
                    num = num * 10 + int(ch)
                if ch == '(':
                    num = helper(li)
                # list 为空时一定进入
                if (not ch.isdigit() and ch != ' ') or len(li) == 0:
                    if sign == '+':
                        stack.append(num)
                    elif sign == '-':
                        stack.append(-num)
                    elif sign == '*':
                        stack.append(stack.pop() * num)
                    elif sign == '/':
                        stack.append(stack.pop() / num)
                    num = 0
                    sign = ch
                if ch == ')':
                    break
            return sum(stack)
        return helper(list(s))


res = Solution().calculate(" 2-1 + 2 ")
print(res)