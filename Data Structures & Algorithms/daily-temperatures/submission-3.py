class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #Brute Force
        #Time complexity: O(n*K)
        #Space complexity: O(n)
        # n = len(temperatures)
        # res = [0] * n

        # for i in range(n):
        #     for j in range(i+1, n):
        #         if temperatures[j] > temperatures[i]:
        #             res[i] = j - i  #  distance
        #             break           #  stop at first warmer day
                    
        # return res
        n = len(temperatures)
        res = [0]*n
        stack = []
        for i in range(n):
            while stack and temperatures[i]>temperatures[stack[-1]]:
                idx = stack.pop()
                res[idx] = i - idx
            stack.append(i)
        return res
