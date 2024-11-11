class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Dictionary to match open and close brackets
        bracket_map = {')': '(', '}': '{', ']': '['}
        stack = []
        
        # Iterate through each character in the string
        for char in s:
            # If it's a closing bracket
            if char in bracket_map:
                # Pop the last element from stack if it's not empty; otherwise, use a dummy value
                top_element = stack.pop() if stack else '#'
                # Check if the popped element matches the corresponding opening bracket
                if bracket_map[char] != top_element:
                    return False
            else:
                # If it's an opening bracket, push it onto the stack
                stack.append(char)
        
        # If the stack is empty, all brackets are matched
        return not stack







    



  

