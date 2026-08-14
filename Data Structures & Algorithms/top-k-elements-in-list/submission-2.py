class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {} #val: freq
        freq = [[] for i in range(len(nums)+1)]
        for i in nums:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
        for i, j in hashmap.items():
            freq[j].append(i)
        res = []
        for i in range(len(freq)-1, 0, -1):
            for j in freq[i]:
                res.append(j)
                if len(res)==k:
                    return res

        