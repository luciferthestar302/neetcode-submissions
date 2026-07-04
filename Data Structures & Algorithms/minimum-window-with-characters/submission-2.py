class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tMap = {}
        for char in t:
            tMap[char] = tMap.get(char,0) + 1
        windowMap = {}
        have, need = 0, len(tMap)
        res = float('inf')
        resLeft, resRight = 0, 0
        left = 0
        for right in range(len(s)):
            # Step 1: add s[right] to windowMap
            windowMap[s[right]] = windowMap.get(s[right], 0) + 1
            # Step 2: check if have increases
            if s[right] in tMap and windowMap[s[right]] == tMap[s[right]]:
                have += 1
            # Step 3: while valid, record and shrink
            while have == need:
                if (right - left + 1) < res:
                    res = right - left + 1
                    resLeft, resRight = left, right
                #shrinking from left, reducing the have if window is not valid and moving left pointer
                windowMap[s[left]] -= 1
                if s[left] in tMap and windowMap[s[left]] < tMap[s[left]]:
                    have -= 1
                left += 1
    
        return s[resLeft:resRight+1] if res != float('inf') else ""
        
        