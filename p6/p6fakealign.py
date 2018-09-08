#!/usr/bin/env python3

# a pair of strings are to be fed in via stdin
# sample invocation:
#     p6  +5  -4  -8 < file_containing_2_lines # (a pair of strings)

import sys

s1 = sys.stdin.readline().strip()
s2 = sys.stdin.readline().strip()

maxlen = max( len(s1), len(s2) )

s1 = s1 + ('-' * (maxlen-len(s1)))
s2 = s2 + ('-' * (maxlen-len(s2)))

print(s1)
print(s2)
