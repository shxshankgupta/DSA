class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        mapT = {}
        for char in t:
            mapT[char] = mapT.get(char, 0) + 1
        mapS = {}
        have, need = 0, len(mapT)
        
        res, res_len = [-1, -1], float("inf")
        left = 0

        for right in range(len(s)):
            char = s[right]
            mapS[char] = mapS.get(char, 0) + 1

            if char in mapT and mapS[char] == mapT[char]:
                have += 1

            while have == need:
                if (right - left + 1) < res_len:
                    res = [left, right]
                    res_len = right - left + 1

                mapS[s[left]] -= 1
                if s[left] in mapT and mapS[s[left]] < mapT[s[left]]:
                    have -= 1
                
                left += 1

        l, r = res
        return s[l : r + 1] if res_len != float("inf") else ""