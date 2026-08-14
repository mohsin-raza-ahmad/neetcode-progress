class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list) # char count: strs
        for i in strs:
            char = [0] * 26
            for j in i:
                char[ord(j) - ord('a')] += 1
            hashmap[tuple(char)].append(i)
        return list(hashmap.values())