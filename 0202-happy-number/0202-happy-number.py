class Solution(object):
    def isHappy(self,n):
    # Create a set to store previously seen numbers to detect cycles
        seen = set()

        while n != 1:
            # Calculate the sum of squares of digits
            n = sum(int(digit) ** 2 for digit in str(n))

            # If we've seen this number before, it's not a happy number
            if n in seen:
                return False

            # Add the current number to the set of seen numbers
            seen.add(n)

        # If we reach 1, it's a happy number
        return True
                
        