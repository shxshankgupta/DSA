class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return s

        combined = s + "#" + s[::-1]
        
        n = len(combined)
        pi = [0] * n
        
        for i in range(1, n):
            j = pi[i - 1]
            while j > 0 and combined[i] != combined[j]:
                j = pi[j - 1]
            if combined[i] == combined[j]:
                j += 1
            pi[i] = j
            
        longest_pal_prefix_len = pi[-1]
        
        suffix_to_add = s[longest_pal_prefix_len:][::-1]
        
        return suffix_to_add + s