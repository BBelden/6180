#!/usr/bin/env python3

## Name:        Ben Belden
## Class ID#:   bpb2v
## Section:     CSCI 6180-001
## Assignment:  Lab #1
## Due:         16:20:00, September 13, 2017
## Purpose: 	Write a program that reads a file whose name is the single command-line
##				argument.  The file contains a description of a multi-layer neural network.
##				Build the described network and perform forward propagation through all
##				layers and then print the outputs of the neurons of the last layer.
## Input:       From preformatted file.  
## Outut:       To terminal.
## 
## File:        p1.py
 
import sys				# for argv[]
import numpy as np		# for array,exp,dot
from math import exp	# for exp

# determine if string can be converted to a number
def isNum(s):
    try:
        float(s)
        return True
    except:  return False

def prsLine(ln):
    cmtInd = ln.find("#")  # remove comments
    if cmtInd != -1:  ln = ln[:cmtInd]
    neuron = list(filter(isNum, ln.split(" ")))
    return (int(neuron[0]), int(neuron[1]), list(map(float, neuron[2:-1])), float(neuron[-1]))

def prsIn(ln):
    cmtInd = ln.find("#")  # remove comments
    if cmtInd != -1:  ln = ln[:cmtInd]
    return list(map(float, filter(isNum, ln.split(" "))))

with open(sys.argv[1],"r") as inFile:
    lines = map(str.rstrip, inFile.readlines())  # remove /n
    lines = list(filter(lambda line: line != "" and not line.startswith("#"), lines))  # rem comments
    neurons = list(map(prsLine, lines[:-1]))  # parse neuron lines
    inVctr = prsIn(lines[-1])  # get input line

biases = []
layers = []
curLyr = -1
for n in neurons:
    if n[0] > curLyr:
        curLyr = n[0]
        biases.append([])
        layers.append([])
    biases[-1].append(n[3])
    layers[-1].append(n[2])

xfrmVctr = np.array([inVctr])
sigFn = lambda x: 1 / (1 + np.exp(-x))
for l, b in zip(layers, biases):
    xfrmVctr = sigFn(np.dot(xfrmVctr, np.array(l).T) + np.array(b))

print(' '.join(map(str, xfrmVctr[0])))

