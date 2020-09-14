# -*- coding: utf-8 -*-


# 变态青蛙跳
def frog_jump(n):
    if n <= 0:
        return
    else:
        return 1 << n - 1
