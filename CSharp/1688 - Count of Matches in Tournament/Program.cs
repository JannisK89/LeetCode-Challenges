﻿
/* 
https://leetcode.com/problems/count-of-matches-in-tournament/

You are given an integer n, the number of teams in a tournament that has strange rules:

If the current number of teams is even, each team gets paired with another team. A total of n / 2 matches are played, and n / 2 teams advance to the next round.
If the current number of teams is odd, one team randomly advances in the tournament, and the rest gets paired. A total of (n - 1) / 2 matches are played,
 and (n - 1) / 2 + 1 teams advance to the next round.
Return the number of matches played in the tournament until a winner is decided.
*/

using System;

namespace _1688
{
    class Program
    {
        static void Main(string[] args)
        {
            var test = new Solution();
            System.Console.WriteLine(test.NumberOfMatches(14));
            System.Console.WriteLine(test.NumberOfMatches(10));
            System.Console.WriteLine(test.NumberOfMatches(7));
        }
    }

    public class Solution
    {
        public int NumberOfMatches(int n)
        {
            int matches = 0;
            while (n > 1)
            {
                if (n % 2 == 0)
                {
                    matches += n / 2;
                    n /= 2;
                }
                else
                {
                    matches += (n - 1) / 2;
                    n = (n - 1) / 2;
                    n++;
                }
            }
            return (matches);
        }
    }
}