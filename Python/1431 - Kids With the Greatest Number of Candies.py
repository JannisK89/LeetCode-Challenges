"""
https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

Given the array candies and the integer extraCandies, where candies[i] represents the number of candies that the ith kid has.

For each kid check if there is a way to distribute extraCandies among the kids such that he or she can have the greatest number
 of candies among them. Notice that multiple kids can have the greatest number of candies.

 Constraints:

2 <= candies.length <= 100
1 <= candies[i] <= 100
1 <= extraCandies <= 50
"""


from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        candyMax = max(candies)
        resultList = []

        for candy in candies:
            if (candy + extraCandies) >= candyMax:
                resultList.append(True)
            
            else:
                 resultList.append(False)
            
        return resultList


test = Solution()

print(test.kidsWithCandies([2,3,5,1,3], 3))

