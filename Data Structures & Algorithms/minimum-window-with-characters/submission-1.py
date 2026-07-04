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
            windowMap[s[right]] = windowMap.get(s[right], 0) + 1
        
            if s[right] in tMap and windowMap[s[right]] == tMap[s[right]]:
                have += 1
            
            while have == need:
                if (right - left + 1) < res:
                    res = right - left + 1
                    resLeft, resRight = left, right
                
                windowMap[s[left]] -= 1
                if s[left] in tMap and windowMap[s[left]] < tMap[s[left]]:
                    have -= 1
                left += 1
    
        return s[resLeft:resRight+1] if res != float('inf') else ""
        
        