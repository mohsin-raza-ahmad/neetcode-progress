'''
thoughts: make a map that maps val: freq. then, make a freq list where each index represents the freq of the val at that index. then make a result list and loop backwards thru freq to get the top k elements.
'''

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        freq = [[] for i in range(len(nums)+1)]
        for num in nums:
            map[num] = 1+map.get(num, 0)
        for num, count in map.items():
            freq[count].append(num)
        res = []
        for i in range(len(freq)-1, -1, -1):
            for j in freq[i]:
                res.append(j)
                if len(res)==k:
                    return res