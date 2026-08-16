class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list) # charcount: list of strings
        for string in strs:
            char_arrangement = [0] * 26
            for char in string:
                char_arrangement[ord(char) - ord("a")] += 1
            hashmap[tuple(char_arrangement)].append(string)
        return list(hashmap.values())
        