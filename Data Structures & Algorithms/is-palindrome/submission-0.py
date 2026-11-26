import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_alnum = re.sub(r'[^a-zA-Z0-9]', '', s).casefold()
        l = 0
        r = len(s_alnum) - 1

        while (l <= r):
            l_ch = s_alnum[l]
            r_ch = s_alnum[r]
            if l_ch == r_ch:
                l += 1
                r -= 1
            else:
                return False

        return True