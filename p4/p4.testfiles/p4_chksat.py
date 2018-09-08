#!/usr/bin/env python3

import sys

clauses = []
with open(sys.argv[1]) as clsFile:
    for line in clsFile:
        line = line.strip()
        if not line.startswith('['):
            continue
        line = line.replace('[',' ')
        line = line.replace(']',' ')
        line = line.replace(',',' ')
        line = line.split()
        clause = [ int(lit) for lit in line ]
        clauses.append(clause)

assignments = {}
with open(sys.argv[2]) as assignmentsFile:
    for line in assignmentsFile:
        if 'assignment' not in line:
            continue
        (unused,var,tval) = line.strip().split()
        var = int(var)
        if var < 0:
            print("You must have printed a lit instead of a variable", var,tval)
            sys.exit(-1)
        if var in assignments:
            print("double assignment for var:", var)
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
            clauseIsSat = True
            break
    if not clauseIsSat:
        print("OOPS; false clause:", clause)
        sys.exit(-1)
print("ALL CLAUSES ARE TRUE")
