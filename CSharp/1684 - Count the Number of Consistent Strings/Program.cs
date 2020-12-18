/*
https://leetcode.com/problems/count-the-number-of-consistent-strings/

You are given a string allowed consisting of distinct characters and an array of strings words. A string is consistent if all characters in the string appear in the string allowed.

Return the number of consistent strings in the array words.


Constraints:
1 <= words.length <= 10^4
1 <= allowed.length <= 26
1 <= words[i].length <= 10
The characters in allowed are distinct.
words[i] and allowed contain only lowercase English letters.

*/

using System;

namespace _1684
{
    class Program
    {
        static void Main(string[] args)
        {
            var test = new Solution();
            
            System.Console.WriteLine(test.CountConsistentStrings("rowd", new string[] { "west", "word", "sword", "r", "doooowwwwrrww" }));
        }
    }

    public class Solution
    {
        public int CountConsistentStrings(string allowed, string[] words)
        {
            int result = 0;
            int counter = 0;

            foreach (var word in words)
            {
                counter = 0;

                foreach (var letter in word)
                {

                    if (!allowed.Contains(letter))
                    {
                        break;
                    }
                    else
                    {
                        counter++;
                    }
                }
                if (counter == word.Length)
                {
                    result++;
                }
            }
            return result;
        }
    }
}
