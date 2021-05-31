from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        needs = {}
        for ch in p:
            needs[ch] = needs.get(ch, 0) + 1
        left = right = 0
        match = 0
        windows = {}
        res = []
        while right < len(s):
            right_str = s[right]
            if right_str in needs:
                windows[right_str] = windows.get(right_str, 0) + 1
                if windows[right_str] == needs[right_str]:
                    match += 1
            right += 1
            while match == len(needs):
                if right - left == len(p):
                    res.append(left)
                left_str = s[left]
                if left_str in needs:
                    windows[left_str] -= 1
                    if windows[left_str] < needs[left_str]:
                        match -= 1
                left += 1
        return res