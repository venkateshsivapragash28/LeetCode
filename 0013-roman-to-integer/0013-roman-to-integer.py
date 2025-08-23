class Solution:
    def romanToInt(self, s: str) -> int:    
        roman = {
            'I'  :  1,
            'V'  :  5,
            'X'  :  10,
            'L'  :  50,
            'C'  :  100,
            'D'  :  500,
            'M'  :  1000
        }
        stack = [roman[s[0]]]

        for i in s[1:]:
            if roman[i] <= stack[-1]:
                stack.append(roman[i])
            else:
                stack[-1] = roman[i] - stack[-1]

        return sum(stack)