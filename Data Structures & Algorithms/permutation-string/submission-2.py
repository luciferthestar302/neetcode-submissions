class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #One edge case will be there when len(s1) > len(s2)
        if len(s1) > len(s2):
            return False

        #Using Hashmap and sliding window we can first store the s1, char and freq in myMap and then we will build first window of s2 string using another hashmap - pMap
        left = 0
        myMap = {}
        pMap = {}
        # Creating a hashmap and storing char and freq of s1
        for right in range(len(s1)):
            myMap[s1[right]] = myMap.get(s1[right],0) + 1
        
        # Creating first window in s2
        for right in range(len(s1)):
            pMap[s2[right]] = pMap.get(s2[right],0) +1
        
        # checking the first window, whether it is matching with myMap
        if myMap == pMap:
            return True
        
        # Creating a window for next values of s2 and then checking it
        for right in range(len(s1), len(s2)):
            pMap[s2[right]] = pMap.get(s2[right],0) +1

            pMap[s2[left]]-=1
            if pMap[s2[left]]==0:
                pMap.pop(s2[left])
            
            #checking if window matches
            if myMap==pMap:
                return True
            left+=1
        return False


        