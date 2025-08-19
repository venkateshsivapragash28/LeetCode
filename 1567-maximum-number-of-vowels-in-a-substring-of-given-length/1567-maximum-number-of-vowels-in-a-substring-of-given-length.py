class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        count = 0
        vowels = ['a', 'e', 'i', 'o', 'u']
        for i in range(k):
            if s[i] in vowels:
                count += 1
        max_count = count
        for i in range(1,len(s) - k + 1):
            x = s[i:i+k]
            if s[i-1] in vowels:
                count-=1
            if s[i+k - 1] in vowels:
                count += 1
            max_count = max(max_count, count)

        return max_count