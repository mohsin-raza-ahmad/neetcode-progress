'''
thoughts: we should use a decreasing deque as each operation is o(1) and it will allow us to skip over elements we dont need to check.
'''

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = collections.deque() # index deque
        l = 0
        r = 0
        res = []
        while r < len(nums):
            # make sure the element going in is in decreasing fasion
            while q and nums[r] > nums[q[-1]]:
                q.pop()
            q.append(r)
            #make sure the deque has valid window indicies
            if l > q[0]:
                q.popleft()
            #append the valid window element
            if r-l+1 == k:
                res.append(nums[q[0]])
                l+=1
            r+=1
        return res
                
                
                
        