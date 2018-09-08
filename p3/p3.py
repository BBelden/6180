#!/usr/bin/env python3

## Name:        Ben Belden
## Class ID#:   bpb2v
## Section:     CSCI 6180-001
## Assignment:  Lab #3
## Due:         09:00:00, October 11, 2017
## Purpose: 	Write a program that determines satisfiability for a set of propositional
##				clauseList.  In the absence of an alternative approach that you prefer, use
##				the DPLL algorithm described below.
## Input:       From preformatted file.  
## Outut:       To terminal.
## 
## File:        p3.py
 
import sys				# for argv[]
import copy				# for deepcopy

def dpllAlgo(clauseList):
    if len(clauseList) == 0:  return []  # empty set
    if any(map(lambda clause: len(clause) == 1, clauseList)):  return None  # empty clause

    ltrlIndx = -1
    unit = None
    for indx, clause in enumerate(clauseList):  # look for unit clause
        if len(clause) == 2:
            ltrlIndx = indx
            unit = clause[0]
            break

    if ltrlIndx != -1:  # unit clause found
        workList = []
        for clause in clauseList:
            if len(clause) == 2 and clause[0] == unit:  continue
            elif unit in clause:  continue
            elif -unit in clause:
                tmpClause = copy.deepcopy(clause)
                tmpClause.remove(-unit)
                workList.append(tmpClause)
            else:  workList.append(clause)
        solutions = dpllAlgo(workList)  # recursion on working list
        if solutions is not None:  return [unit] + dpllAlgo(workList)
        else:  return None

    else:  # unit clause not found, choose variable heuristically
        heurVar = clauseList[0][0]
        workList = [[heurVar, 0]] + copy.deepcopy(clauseList)
        solutions = dpllAlgo(workList)
        if solutions is not None:  return [heurVar] + solutions
        else:
            workList[0][0] = -heurVar
            solutions = dpllAlgo(workList)
            if solutions is not None:  return [-heurVar] + solutions
            else:  return None

inFile = sys.argv[1]

def parseDimacs(inFile):
    with open(inFile, 'r') as iFile:
        for line in iFile.readlines():
            line = line.rstrip()
            if len(line) == 0 or line[0] == 'c':  continue
            if line[0] == 'p':  continue
            yield [int(i) for i in line.split()]

clauseList = list(parseDimacs(inFile))
solutions = dpllAlgo(clauseList)
if solutions is None:  print("UNSATISFIABLE")
else:
    for var in sorted(set(solutions)):  print("{} {}".format(abs(var), int(var > 0)))

