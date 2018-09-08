#!/usr/bin/env python3

## Name:        Ben Belden
## Class ID#:   bpb2v
## Section:     CSCI 6180-001
## Assignment:  Lab #5
## Due:         16:20:00, November 13, 2017
## Purpose:     Write a program that reads a pair of strings from stdin 
##				(which marowLen be re-directed from a file). Each string will 
##				be on a single line browLen itself. Be sure to strip off 
##				whitespace at each end of the strings, including newlines.
## Input:       From preformatted file.  
## Outut:       To terminal.
## 
## File:        p5.py

import sys

matchVal = sys.argv[1]
mismatchPen = sys.argv[2]
gapPen = sys.argv[3]
topOut = []
btmOut = []
selection = ['d', 'l', 't']
matrix = []
row = input()
col = input()

for i in range(0, len(col)+1):
    matrix.append([])
    for j in range(0, len(row)+1):
        matrix[i].append([-1])
for i in range(0, len(row) + 1):  matrix[0][i] = [0]
for i in range (0, len(col) + 1):  matrix[i][0] = [0]

for r in range(1, len(col)+1):
    for c in range(1, len(row)+1):
        diag = matrix[r-1][c-1][0]
        if row[c-1] == col[r-1]:  diag += int(matchVal)
        else:  diag += int(mismatchPen)
        left = matrix[r][c-1][0] + int(gapPen)
        top = matrix[r-1][c][0] + int(gapPen)
        MAX = [diag, left, top]
        for i in range(0, len(MAX)):
            if MAX[i] == max(MAX):
                matrix[r][c].append(selection[i])
                break
        matrix[r][c][0] = max(MAX)

colLen = len(col)
rowLen = len(row)

while colLen != 0 or rowLen != 0:
    if colLen == 0:
        topOut.append(row[rowLen-1])
        btmOut.append('-')
        rowLen -= 1
    elif rowLen == 0:
        topOut.append('-')
        btmOut.append(col[colLen-1])
        colLen -= 1
    else:
        if matrix[colLen][rowLen][1] == 'd': 
            topOut.append(row[rowLen-1])
            btmOut.append(col[colLen-1])
            rowLen -= 1
            colLen -= 1
        elif matrix[colLen][rowLen][1] == 'l':
            topOut.append(row[rowLen-1])
            btmOut.append('-')
            rowLen -= 1
        else:
            topOut.append('-')
            btmOut.append(col[colLen-1])
            colLen -= 1

for t in topOut[::-1]:  sys.stdout.write(t)
print()
for b in btmOut[::-1]:  sys.stdout.write(b)
print()

