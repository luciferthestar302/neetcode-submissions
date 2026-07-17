class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        my_stack = []
        for token in tokens:
            if token in['+','-','/','*']:
                b = my_stack.pop()
                a = my_stack.pop()
                #Apply Operator
                if token=='+':
                    my_stack.append(a+b)
                elif token=='-':
                    my_stack.append(a-b)
                elif token=='/':
                    my_stack.append(int(a/b))
                elif token=='*':
                    my_stack.append(int(a*b))
            else:
                my_stack.append(int(token))
        return my_stack[-1] #returning the top element

        