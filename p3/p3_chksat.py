#!/usr/bin/env python

import sys

clsFile = open(sys.argv[1])

clauses = []
line = clsFile.readline()
while line:
    line = line.strip()
    if line[0] == 'c'  or  line[0] == 'p':
        line = clsFile.readline()
        continue
    line = line.split()
    if line[-1] != "0":
        while True:
            nextLine = clsFile.readline().strip()
            if not nextLine:
                print "NON-TERMINATING CLAUSE AT:", line
                sys.exit(-1)
            line += nextLine.split()
            if line[-1] == "0":
                break
    clause = [ int(lit) for lit in line if lit != "0" ]  # may not want this line
    clauses.append(clause)
    line = clsFile.readline()
# print clauses

assignmentsFile = open(sys.argv[2])

assignments = {}
for line in assignmentsFile:
    (var,tval) = line.split()
    var = int(var)
    if var < 0:
        print "You must have printed a lit instead of a variable", var,tval
        sys.exit(-1)
    if var in assignments:
        print "double assignment for var:", var
        break
    assignments[var] = int(tval)

for clause in clauses:
    clauseIsSat = False
    for lit in clause:
        var =  lit  if lit > 0  else  -lit  # var = abs(lit) may be better :-)
        if var not in assignments:  # simply not assigned a value
            continue
        tval = assignments[var]
        if lit < 0:  # need to reverse the tval
            tval =  0  if tval else  1
        if tval:
            # print "found", lit, tval
            clauseIsSat = True
            break
    if not clauseIsSat:
        print "OOPS; false clause:", clause
        sys.exit(-1)
print "ALL CLAUSES ARE TRUE"
