'''
problem: without sorting, i need to get the top k elemets in a list. 
to do: make a hashmap that maps values to its frequency. then, i can make a bucket list where the indexes rep the frequnecy of the values at such index. Next, loop back thru this bucket list and append the last k elements to a result list until this result list is k elements long.
'''


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        freq = [[] for i in range(len(nums)+1)]
        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1
        for i, j in hashmap.items():
            freq[j].append(i)
        res = []
        for i in range(len(freq)-1, -1, -1):
            for j in freq[i]:
                res.append(j)
                if len(res) == k:
                    return res