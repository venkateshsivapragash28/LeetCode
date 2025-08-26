class Solution:
    def getHint(self, secret: str, guess: str) -> str:

        counter1 = {}
        counter2 = {}

        bulls = 0
        for i in range(len(str(secret))):
            if secret[i] in counter1:
                counter1[secret[i]]+=1
            elif secret[i] not in counter1:
                counter1[secret[i]] = 1

            if guess[i] in counter2:
                counter2[guess[i]]+=1
            elif guess[i] not in counter2:
                counter2[guess[i]] = 1

            if secret[i] == guess[i]:
                bulls += 1

        cows = 0
        for i in counter1:
            if i in counter2:
                cows += min(counter1[i], counter2[i])
            
        cows = cows-bulls

        return f'{bulls}A{cows}B'