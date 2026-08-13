class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        '''Initial thoughts: I see that I need to store data to look at later. Since I only need to know its existence, i can use a set
        '''
        hashset = set()
        for i in nums:
            if i in hashset:
                return True
            else:
                hashset.add(i)
        return False