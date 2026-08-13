class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap_1 = {}
        hashmap_2 = {}
        for i in s:
            if i in hashmap_1:
                hashmap_1[i] += 1
            else:
                hashmap_1[i] = 1
        for i in t:
            if i in hashmap_2:
                hashmap_2[i] += 1
            else:
                hashmap_2[i] = 1
        return hashmap_1 == hashmap_2