class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        # Frequency map for characters needed from string t
        target_count = {}
        for char in t:
            target_count[char] = target_count.get(char, 0) + 1
        
        required = len(target_count)
        formed = 0
        
        # Window frequency map
        window_count = {}
        
        # Result variables
        min_length = float('inf')
        min_window = ""
        
        left = 0
        for right in range(len(s)):
            # Add current character to window
            char = s[right]
            window_count[char] = window_count.get(char, 0) + 1
            
            # If this character meets the requirement in t, increment formed
            if char in target_count and window_count[char] == target_count[char]:
                formed += 1
                
            # Contract the window from the left while the window is valid
            while formed == required:
                # Update minimum window if current is smaller
                if right - left + 1 < min_length:
                    min_length = right - left + 1
                    min_window = s[left:right + 1]
                
                # Remove leftmost character from window
                left_char = s[left]
                window_count[left_char] -= 1
                
                # If removing this character breaks the valid window, decrement formed
                if left_char in target_count and window_count[left_char] < target_count[left_char]:
                    formed -= 1
                    
                left += 1
                
        return min_window   
        