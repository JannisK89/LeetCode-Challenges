
# https://leetcode.com/problems/single-number/

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(0, len(nums), 2):
            if i != len(nums)-1:
                if nums[i] != nums[i+1]:
                    return nums[i]

        return nums[-1]


test = Solution()

print(test.singleNumber([-1, -6, -1, -6, 7, 7, 8, 4, 3, 2, 1, 2, 3, 4, 1]))

