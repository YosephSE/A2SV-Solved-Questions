class Solution:
    def minWindow(self, s, t):
        ans = (0, float('inf'))
        left, tar, win = 0, Counter(t), Counter()

        for right in range(len(s)):
            ch = s[right]
            win[ch] += 1

            while all(win[c] >= tar[c] for c in tar):
                if ans[1] >= right - left + 1:
                    ans = (left, right - left + 1)

                remch = s[left]
                win[remch] -= 1
                if win[remch] == 0:
                    del win[remch]

                left += 1

        return "" if ans[1] == float('inf') else s[ans[0]:ans[0] + ans[1]]