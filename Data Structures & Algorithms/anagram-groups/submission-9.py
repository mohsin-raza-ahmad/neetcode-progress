'''
thoughts: make a map that will map character arrangements to a list of strings that follow this arrangement. return the list of the maps vals.
'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list)
        for string in strs:
            char_arr = [0] * 26
            for char in string:
                char_arr[ord(char) - ord('a')] += 1
            map[tuple(char_arr)].append(string)
        return list(map.values())