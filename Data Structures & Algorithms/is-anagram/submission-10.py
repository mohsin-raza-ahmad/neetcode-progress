class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        Thoughts: I need to keep track of both the existence AND freq of character in each string. Thus, ill make a hashmap to monitor this. At the end, I can compare both hashmaps to concluse if each string is an anagram of each other.
        '''
        hash1 = {}
        hash2 = {}
        for i in s:
            if i in hash1:
                hash1[i] += 1
            else: 
                hash1[i] = 1
        for i in t:
            if i in hash2:
                hash2[i] += 1
            else: 
                hash2[i] = 1
        return hash1 == hash2