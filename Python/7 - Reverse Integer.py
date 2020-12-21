"""
https://leetcode.com/problems/reverse-integer/

Given a 32-bit signed integer, reverse digits of an integer.

Note:
Assume we are dealing with an environment that could only store integers 
within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, 
assume that your function returns 0 when the reversed integer overflows.
"""


class Solution:
    def reverse(self, x: int) -> int:
        MAXINT = 2_147_483_647
        isNegative = False

        if x < 0:
            isNegative = True

        reversedValues = int(str(abs(x))[::-1])

        if int(reversedValues) > MAXINT:
            return 0

        elif isNegative:
            return int(reversedValues) * -1

        else:
            return int(reversedValues)


test = Solution()
print(test.reverse(123456))
print(test.reverse(-123456))
print(test.reverse(2_147_483_647))
print(test.reverse(-2_147_483_647))
print(test.reverse(-7_463_847_412))
print(test.reverse(7_463_847_412))
print(test.reverse(-8_463_847_412))
print(test.reverse(8_463_847_412))
print(test.reverse(0))
