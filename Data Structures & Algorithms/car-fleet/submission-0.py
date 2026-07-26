class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[pos,sp] for pos, sp in zip(position, speed)]
        stack = []
        for pos, sp in sorted(pair)[::-1]: #Sorting in reverse order
            stack.append((target-pos)/sp)
            if len(stack) >=2 and stack[-1] <=stack[-2]:
                stack.pop()
        return len(stack)
        