class Solution:
    def characterReplacement(self, s: s, k: int) -> int:
        myMap = {}
        left = 0
        res = 0

        for right in range(len(s)):
            #expanding window from right, initially both left and right pointers are at index = 0
            myMap[s[right]] = myMap.get(s[right],0) + 1
            #  window_size = right-left+1 ; a window is valid when: (right - left +1)-max_freq <=k
            max_freq = max(myMap.values())
            if (right - left + 1 - max_freq <=k):
                res = max(res, right-left+1)
            else:
                myMap[s[left]]-=1
                left+=1
        return res





        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # This code fails because we are asked to find out the longest consecutive substring, and it will not give expected output, fore.g: s = "AABABBA" and K = 1, expected output = 5 but mine will give 4
        
        # myMap = {}
        # for char in s:
        #     if char in myMap:
        #         myMap[char]+=1
        #     else:
        #         myMap[char] = 1
        # max_char = max(myMap, key = myMap.get)
        # max_count = myMap[max_char]
        # # return (max_count + k) --> this will not work if a string contains a char which is repeating, e.g: str = "AAAAAA" and k=1
        # if len(myMap) == 1: 
        #     return max_count
        # else: 
        #     return (max_count + k)
        
        
        
        
        
        
        
        
        
        
      