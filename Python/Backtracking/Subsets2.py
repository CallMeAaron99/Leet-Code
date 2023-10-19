from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        res = []
        subset = []
        def dfs(i):

            if i == len(nums):
                res.append(subset.copy())
                return
            
            # subsets that include nums[i]
            subset.append(nums[i])
            dfs(i + 1)

            # subsets that don't include nums[i]
            subset.pop()

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            
            dfs(i + 1)

        dfs(0)
        return res
    
s = Solution()
s.subsetsWithDup([1, 2, 2])