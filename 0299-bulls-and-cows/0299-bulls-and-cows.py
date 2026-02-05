class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        secret_freq, guess_freq = {}, {}
        correct_guesses, inplace_guesses = 0, 0
        for i in range(len(secret)):
            secret_freq[secret[i]] = secret_freq.get(secret[i], 0) + 1
            guess_freq[guess[i]] = guess_freq.get(guess[i], 0) + 1
        for i in guess_freq:
            if guess_freq[i] >= secret_freq.get(i, 0):
                correct_guesses += secret_freq.get(i, 0)
            else:
                correct_guesses += guess_freq.get(i, 0)
        for i in range(len(guess)):
            if guess[i] == secret[i]:
                inplace_guesses += 1
        return f"{inplace_guesses}A{correct_guesses - inplace_guesses}B"
        
            
            

        