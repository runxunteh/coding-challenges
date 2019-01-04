#https://www.hackerrank.com/challenges/introduction-to-regex/problem
"""
Test cases:
4
4.0O0
-1.00
+4.54
SomeRandomStuff
"""

import re
x=int(input())
for i in range(x):
    print(bool(re.match(r'^[-+]?[0-9]*\.[0-9]+$', input())))
