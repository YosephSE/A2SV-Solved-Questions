class Solution(object):
    def wordPattern(self, pattern, s):
        words = s.split()
        
        if len(pattern) != len(words):
            return False
        
        letter_to_word = {}
        word_to_letter = {}
        
        for p, w in zip(pattern, words):
            if p in letter_to_word and letter_to_word[p] != w:
                return False
            if w in word_to_letter and word_to_letter[w] != p:
                return False
            
            letter_to_word[p] = w
            word_to_letter[w] = p
        
        return True
