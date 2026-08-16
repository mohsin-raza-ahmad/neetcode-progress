class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {} # val: freq
        freq = [[] for i in range(len(nums)+1)]
        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1
        for val, index in hashmap.items():
            freq[index].append(val)
        result = []
        for position in range(len(freq)-1, 0, -1):
            for value in freq[position]:
                result.append(value)
                if len(result) == k:
                    return result