'''
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
Note:
You may assume both s and t have the same length.
'''

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d1 = {}
        d2 = {}

        for i in range(len(s)):
            c1 = s[i]
            c2 = t[i]

            if c1 in d1:
                if d1[c1] != c2 or d2[c2] != c1:
                    return False

            else:
                if c2 in d2:
                    return False
                d1[c1] = c2
                d2[c2] = c1
        return True

