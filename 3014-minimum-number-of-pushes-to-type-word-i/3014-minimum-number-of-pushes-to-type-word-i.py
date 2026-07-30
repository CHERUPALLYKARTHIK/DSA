class Solution:
    def minimumPushes(self, word: str) -> int:
        n = len(word)
        pushes = 0
        
        # Every group of 8 letters requires 1 additional push per character
        for i in range(n):
            pushes += (i // 8) + 1
            
        return pushes