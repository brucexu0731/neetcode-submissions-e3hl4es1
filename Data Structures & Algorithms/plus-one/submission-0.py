class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        carry = 0
        digits[-1] += 1
        if digits[-1] == 10:
            carry = 1
            digits[-1] = 0
            digit = len(digits) - 2

            while carry and digit >= 0:
                digits[digit] += 1
                if digits[digit] == 10:
                    carry = 1 
                    digits[digit] = 0
                    digit -= 1
                else:
                    carry = 0
            
            if digit == -1:
                digits = [1] + digits
        
        return digits

