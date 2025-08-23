class Solution:
    def convert(self, s: str, n: int) -> str:
        if n == 1 or n >= len(s):
            return s
        dick = {}
        i = 0
        while i < len(s) :
            count = 1
            if count == 1 and i < len(s):
                while count < n and i < len(s):
                    if count in dick:
                        dick[count] += s[i]
                    else:
                        dick[count] = s[i]
                    count += 1
                    i += 1
            if count == n and i < len(s):
                while count > 1 and i < len(s):
                    if count in dick:
                        dick[count] += s[i]
                    else:
                        dick[count] = s[i]
                    count -= 1
                    i += 1

        return ''.join(dick.values())
