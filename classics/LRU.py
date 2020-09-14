"""
1. 用 dict 和 list
2. list 中最后一个元素表示最近使用
"""

class LRUCache:

    def __init__(self, capacity):
        self.cache = {}
        self.used_list = []
        self.capacity = capacity

    def get(self, key):
        if key in self.cache:
            if key != self.used_list[-1]:
                self.used_list.remove(key)
                self.used_list.append(key)
            return self.cache[key]
        else:
            return -1

    def set(self, key, value):
        if key in self.cache:
            self.used_list.remove(key)
        elif len(self.cache) == self.capacity:
            self.cache.pop(self.used_list.pop(0))
        self.used_list.append(key)
        self.cache[key] = value