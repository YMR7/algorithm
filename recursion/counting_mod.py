# -*- coding: utf-8 -*-


# 求 base^index%mod

# (ab)%c == [(a%c)(b%c)]%c
def counting_mod(base, index, mod):
    # 代数进去发现成立 ，直接用，不用去推导
    base %= mod
    result = 1
    while index != 0:
        # index & 1 == index % 1
        if index & 1:
            result = result * base % mod
        index >>= 1
        base = base * base % mod
    return result


if __name__ == '__main__':
    a, b, c = map(int, input().split())
    print(counting_mod(a, b, c))