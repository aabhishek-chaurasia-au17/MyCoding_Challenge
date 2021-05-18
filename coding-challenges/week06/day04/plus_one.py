class Solution:
    def plusOne(self, digits):
        new = ''
        new_digits = []
        if digits[-1] != 9:
            digits[-1] += 1
            return digits
        else:
            for i in digits:
                new += str(i)
            new = str(int(new)+1)
            for i in new:
                new_digits.append(int(i))
            return new_digits
            
       
            