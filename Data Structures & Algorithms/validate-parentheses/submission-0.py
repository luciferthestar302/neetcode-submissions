class Solution:
    def isValid(self, s: str) -> bool:
        #We need hashmap to store brackets
        my_Map = {')':'(', '}':'{', ']':'['}
        my_stack = []
        for char in s:
            if char in my_Map:
                if my_stack and my_stack[-1]==my_Map[char]:
                    my_stack.pop()
                else:
                    return False
            else:
                my_stack.append(char)
        return len(my_stack)==0 #if all brackets are matched so stack is empty and it will return True
        