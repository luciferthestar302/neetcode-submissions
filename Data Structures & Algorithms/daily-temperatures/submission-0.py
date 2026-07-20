class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n

        for i in range(n):
            for j in range(i+1, n):
                if temperatures[j] > temperatures[i]:
                    res[i] = j - i  #  distance
                    break           #  stop at first warmer day
                    
        return res
        