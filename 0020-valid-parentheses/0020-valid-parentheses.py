class Solution(object):
    def isValid(self,s):
        stack = []  # stack for appending open opening bracket "(,{,["
    
        for char in s:
            if char in "({[":  # for opening bracket, push it to the stack
                stack.append(char)
            else:  # If it is a closing bracket
                if not stack:  # Stack is empty, invalid case
                    return False
            
                top_element = stack.pop()
            
            # Check if the popped opening bracket matches the current closing bracket
                if char == ')' and top_element != '(':
                    return False
                elif char == '}' and top_element != '{':
                    return False
                elif char == ']' and top_element != '[':
                    return False
    
    # If the stack is empty, all the brackets were properly matched
        return not stack
