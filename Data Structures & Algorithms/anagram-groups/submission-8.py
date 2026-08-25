class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = defaultdict(list)
        for string in strs:
            char_arr = [0] * 26
            for char in string:
                char_arr[ord(char) - ord('a')] += 1
            hash[tuple(char_arr)].append(string)
        return list(hash.values())