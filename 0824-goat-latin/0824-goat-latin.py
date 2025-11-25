class Solution:
    def toGoatLatin(self, sentence: str) -> str:

        words = sentence.split()

        vowels = {'a', 'e', 'i', 'o', 'u'}

        for index, word in enumerate(words):
            if word[0].lower() in vowels:
                new = word + 'ma'

            else:
                new = word[1:] + word[0] + 'ma'
                
            new += 'a' * (index + 1)
            words[index] = new


        return ' '.join(words)


            