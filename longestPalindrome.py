class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        reslen = 0 #result len

        for I in range(len(s)):
            # odd length
            l, r = i, i  #left and right
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > reslen:
                    result = s[l : r+1]
                    reslen = r - l + 1
                l -= 1
                r += 1

                # odd length
            l, r = i, i + 1 #left and right
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > reslen:
                    result = s[l : r+1]
                    reslen = r - l + 1
                l -= 1
                r += 1
        return result