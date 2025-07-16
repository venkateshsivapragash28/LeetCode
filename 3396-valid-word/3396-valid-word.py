class Solution(object):
    def isValid(self, words):
        letter_count = 0
        vowel_count = 0
        consonant_count = 0
        letters = [48,49,50,51,52,53,54,55,56,57,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122]
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        consonants = [
    'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm',
    'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z',
    'B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M',
    'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z'
]
        if len(words) < 3:
            return False
        for i in words:
            if ord(i) in letters:
                letter_count += 1
            if i in vowels:
                vowel_count +=1
            if i in consonants:
                consonant_count += 1
        
        if letter_count == len(words) and vowel_count >= 1 and consonant_count >= 1:
            return True
        else:
            return False
                 