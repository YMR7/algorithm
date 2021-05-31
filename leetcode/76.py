"""
滑动窗口
int left = 0, right = 0;

while (right < s.size()) {
    window.add(s[right]);
    right++;
    
    while (valid) {
        window.remove(s[left]);
        left++;
    }
}
"""


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        size = len(s)
        left = right = 0
        min_len = float('inf')
        match = 0
        start = 0
        needs = {}
        for ch in t:
            needs[ch] = needs.get(ch, 0) + 1
        windows = {}
        while right < size:
            cur_str = s[right]
            if cur_str in needs:
                windows[cur_str] = windows.get(cur_str, 0) + 1
                if windows[cur_str] == needs[cur_str]:
                    match += 1
            right += 1
            while match == len(needs):
                if (right - left) < min_len:
                    start = left
                    min_len = right - left
                left_str = s[left]
                if left_str in needs:
                    windows[left_str] -= 1
                    if windows[left_str] < needs[left_str]:
                        match -= 1
                left += 1
        return "" if min_len == float('inf') else s[start:start + min_len]


if __name__ == '__main__':
    res = Solution().minWindow('cabwefgewcwaefgcf', 'cae')
    print(res)