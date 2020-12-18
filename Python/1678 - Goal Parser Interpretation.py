"""
https://leetcode.com/problems/goal-parser-interpretation/

You own a Goal Parser that can interpret a string command. The command consists of an alphabet of "G", "()" and/or "(al)" in some order. 
The Goal Parser will interpret "G" as the string "G", "()" as the string "o", and "(al)" as the string "al". The interpreted strings are then concatenated in the original order.

Given the string command, return the Goal Parser's interpretation of command.

Constraints:

1 <= command.length <= 100
command consists of "G", "()", and/or "(al)" in some order.
"""


class Solution:
    def interpret(self, command: str) -> str:
        interpreted = command.replace('()', 'o').replace('(al)', 'al')
        return interpreted


test = Solution()

print(test.interpret('G()()(al)'))
print(test.interpret('(al)(al)(al)G(al)(al)(al)(al)G()()(al)()()G()()()()G()'))
