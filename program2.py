class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Define the value for each Roman numeral symbol
        roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total = 0
        prev_value = 0
        
        # Iterate through the string in reverse order
        for char in reversed(s):
            # Get the integer value of the current Roman numeral
            current_value = roman_map[char]
            
            # If the current value is less than the previous value, it means subtraction case
            if current_value < prev_value:
                total -= current_value
            else:
                total += current_value
            
            # Update previous value to the current one
            prev_value = current_value
        
        return total
