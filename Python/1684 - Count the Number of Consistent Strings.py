"""
https://leetcode.com/problems/count-the-number-of-consistent-strings/

You are given a string allowed consisting of distinct characters and an array of strings words. A string is consistent if all characters in the string appear in the string allowed.

Return the number of consistent strings in the array words.


Constraints:
1 <= words.length <= 10^4
1 <= allowed.length <= 26
1 <= words[i].length <= 10
The characters in allowed are distinct.
words[i] and allowed contain only lowercase English letters.
"""
from typing import List


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        counter = 0
        result = 0

        for word in words:
            counter = 0

            for letter in word:
                if (letter not in allowed):
                    break
                else:
                    counter += 1

            if counter >= len(word):
                result += 1

        return result


test = Solution()
print(test.countConsistentStrings(
    'abc', ['test', 'bace', 'bacacab', 'bbaaaccaaccabbab', 'baceabab', 'cab']))
