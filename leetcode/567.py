class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        needs = {}
        for ch in s1:
            needs[ch] = needs.get(ch, 0) + 1
        left = right = 0
        match = 0
        windows = {}
        while right < len(s2):
            cur_str = s2[right]
            if cur_str in needs:
                windows[cur_str] = windows.get(cur_str, 0) + 1
                if windows[cur_str] == needs[cur_str]:
                    match += 1
            right += 1
            while match == len(needs):
                if right - left == len(s1):
                    return True
                left_str = s2[left]
                if left_str in needs:
                    windows[left_str] -= 1
                    if windows[left_str] < needs[left_str]:
                        match -= 1
                left += 1
        return False