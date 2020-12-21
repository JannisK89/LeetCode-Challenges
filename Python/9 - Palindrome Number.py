"""
https://leetcode.com/problems/palindrome-number/

Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:

        return str(x)[::-1] == str(x)


test = Solution()

print(test.isPalindrome(1342))  # False
print(test.isPalindrome(1112223333222111))  # True
print(test.isPalindrome(12344321))  # True
print(test.isPalindrome(1234321))  # True
print(test.isPalindrome(-1234321))  # False
