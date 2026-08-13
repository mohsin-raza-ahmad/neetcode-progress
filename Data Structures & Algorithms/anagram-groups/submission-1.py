class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
       '''
       Thoughts:
       I need to keep track of both val and freq of each char in each string in strs. Thus, hashmap, where the key is the freq of chars, and the val is the anagrams. To get the freq of chars, i can make a list of 26 indexes (26 letters), and update position of the char.
       '''
       hash = defaultdict(list)
       for s in strs:
        char_count = [0] * 26
        for c in s:
            char_count[ord(c) - ord('a')] += 1 #update num of char
        hash[tuple(char_count)].append(s)
       return list(hash.values())
