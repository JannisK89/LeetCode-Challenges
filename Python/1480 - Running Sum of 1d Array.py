"""
https://leetcode.com/problems/running-sum-of-1d-array/

Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.
"""

from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        total = 0
        runningSumList = []

        for num in nums:
            total += num
            runningSumList.append(total)

        return runningSumList


test = Solution()

print(test.runningSum([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(test.runningSum([1111, 2222, 3333, 4444, 5555]))
