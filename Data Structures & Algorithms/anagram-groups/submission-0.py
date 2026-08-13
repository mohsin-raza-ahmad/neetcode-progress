class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list) # why? cuz i need chars: list of anagrams
        for i in strs: # for every string
            char_count = [0] * 26 # make a char count
            for j in i: # for each char
                char_count[ord(j) - ord('a')] += 1 # add the num of chars u have
            hashmap[tuple(char_count)].append(i) # if same num of chars, append string, if not, new freq of chars
        return list(hashmap.values())


            