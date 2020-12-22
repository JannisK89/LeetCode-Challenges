"""
https://leetcode.com/problems/valid-parentheses/

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict = {')': '(', '}': '{', ']': '['}

        for parentheses in s:
            if parentheses in (')', '}', ']') and len(stack) == 0:
                return False

            if parentheses in ('{', '[', '('):
                stack.append(parentheses)

            elif len(stack) > 0:
                if dict[parentheses] != stack.pop():
                    return False

        return True if len(stack) == 0 else False


test = Solution()
print(test.isValid('{{[[(())]]}}'))  # True
print(test.isValid('{{[[(()))]}}'))  # False
print(test.isValid('{{}[][(()))}'))  # False
print(test.isValid('{{}[][(()))'))  # False
print(test.isValid(')'))  # False
print(test.isValid(')('))  # False
print(test.isValid('('))  # False
