class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        dick = {
            '2' : 'abc',
            '3' : 'def',
            '4' : 'ghi',
            '5' : 'jkl',
            '6' : 'mno',
            '7' : 'pqrs',
            '8' : 'tuv',
            '9' : 'wxyz'
        }
        n = len(digits)
        res = []
        def f(index, s):
            if index == n:
                res.append(s)
                return

            current = dick[digits[index]]

            for char in current:
                s += char
                f(index + 1, s)
                s = s[:-1]

        f(0,'')

        return res

