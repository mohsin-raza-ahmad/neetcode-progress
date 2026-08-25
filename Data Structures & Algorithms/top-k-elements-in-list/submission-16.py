class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = {}
        freq = [[] for i in range(len(nums)+1)]
        for num in nums:
            if num in hash:
                hash[num] += 1
            else:
                hash[num] = 1
        for i,j in hash.items():
            freq[j].append(i)
        res = []
        for i in range(len(freq)-1,-1,-1):
            for j in freq[i]:
                res.append(j)
                if len(res) == k:
                    return res
