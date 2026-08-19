'''
problem: need to check if two strings have the same amount of letters and same type of letters.
soln: make 2 hashmaps that map a char to its freq. at the end, if both hashmaps are the same, its an anagram.
'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash1 = {}
        hash2 = {}
        for letter in s:
            if letter in hash1:
                hash1[letter] += 1
            else:
                hash1[letter] = 1
        for letter in t:
            if letter in hash2:
                hash2[letter] += 1
            else:
                hash2[letter] = 1
        return hash1 == hash2
            
        