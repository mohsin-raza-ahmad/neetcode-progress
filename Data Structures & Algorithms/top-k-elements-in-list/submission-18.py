class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        freq = [[] for i in range(len(nums)+1)]
        for num in nums:
            map[num] = 1 + map.get(num, 0)
        for i, j in map.items():
            freq[j].append(i)
        res = []
        for i in range(len(freq)-1, -1, -1):
            for j in freq[i]:
                res.append(j)
                if len(res) == k:
                    return res