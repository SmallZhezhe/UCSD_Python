"""Simple example of using UserString"""
from collections import UserString
from functools import total_ordering


@total_ordering
class StringIgnoreCase(UserString):

    def __eq__(self, other):
        return self.data.lower() == other.lower()

    def __lt__(self, other):
        return self.data.lower() < other.lower()


"""
from user_string import StringIgnoreCase
s1 = StringIgnoreCase("IGNORE THE CASE")
s2 = StringIgnoreCase("ignore the case")
s3 = StringIgnoreCase("Ignore The Case")
s1 == s2 == s3
s1.lower() == s2.upper()
"abc" < "DEF"
s4 = StringIgnoreCase("abc")
s5 = StringIgnoreCase("DEF")
s4 < s5

s1
s1[7:10]
s4
s5
s4 * 3
s4 += s5
s4

"""
