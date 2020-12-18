/*
https://leetcode.com/problems/goal-parser-interpretation/

You own a Goal Parser that can interpret a string command. The command consists of an alphabet of "G", "()" and/or "(al)" in some order. 
The Goal Parser will interpret "G" as the string "G", "()" as the string "o", and "(al)" as the string "al". The interpreted strings are then concatenated in the original order.

Given the string command, return the Goal Parser's interpretation of command.
*/

namespace _1678
{
    class Program
    {
        static void Main(string[] args)
        {
            var test = new Solution();

            System.Console.WriteLine(test.Interpret("G()(al)"));
            System.Console.WriteLine(test.Interpret("()G()()()()()(al)()()(al)"));
        }
    }

    public class Solution
    {
        public string Interpret(string command)
        {
            command = command.Replace("()", "o").Replace("(al)", ("al"));

            return command;
        }
    }
}
