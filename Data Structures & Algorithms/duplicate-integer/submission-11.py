class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_set = set()
        for num in nums:
            if num in nums_set:
                return True
            else:
                nums_set.add(num) # puts the num into the set if its not in it.
        return False