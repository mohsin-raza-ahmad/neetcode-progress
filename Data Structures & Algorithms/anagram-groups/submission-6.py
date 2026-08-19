'''
problem: without sorting, return a list of anagrams together
to do: make a hashmap that maps the char arrangement of each string to the list of strings. then return a list of the values of the hashmap
'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list) 
        for string in strs:
            char_arr = [0] * 26
            for char in string:
                char_arr[ord(char) - ord('a')] += 1
            hashmap[tuple(char_arr)].append(string)
        return list(hashmap.values())
        