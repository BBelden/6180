#!/usr/bin/env python3

## Name:        Ben Belden
## Class ID#:   bpb2v
## Section:     CSCI 6180-001
## Assignment:  Lab #2
## Due:         16:20:00,September 27,2017
## Purpose: 	Write a program that reads a file whose name is the single command-line
##				argument.  The file contains a description of a multi-layer neural network.
##				Build the described network and perform forward propagation through all
##				layers and then print the outputs of the neurons of the last layer.
##				Enhanced for back propagation,training,and prediction.
## Input:       From preformatted file.  
## Outut:       To terminal.
## 
## File:        p2.py
 
import sys				# for argv[]
import numpy as np		# for array,exp,dot
from math import exp	# for exp

def sigFn(x):  return 1 / (1+np.exp(-x))

def neuronOut(net,inVectr):
    out = []
    xfrmVectr = inVectr
    for layer in layers:
        xfrmVectr = sigFn(layer["biases"] + np.dot(xfrmVectr,layer["weights"].T))
        out.append(xfrmVectr)
    return out

def nnIsRight(net,testData):
    results = []
    for row in testData:
        out = neuronOut(net,row[:-1])[-1]
        results.append(np.argmax(out) == int(row[-1]))
    return (int(sum(results)),len(results))

nnDescr = sys.argv[1]
dataFile = sys.argv[2]
lowTrain = int(sys.argv[3])
hiTrain = int(sys.argv[4])
lowTest = int(sys.argv[5])
hiTest = int(sys.argv[6])
nEpochs = int(sys.argv[7])
intrnlFlag = int(sys.argv[8]) == 1

with open(nnDescr,"r") as inFile:
    cLayer = -1
    layers = []
    for line in inFile.readlines():
        cmntIndx = line.find("#")
        if cmntIndx != -1:  line = line[:cmntIndx]
        line = line.strip().split()
        if len(line) == 0:  continue
        if int(line[0]) > cLayer:
            layers.append({"weights": [],"biases": []})
            cLayer+=1
        layers[cLayer]["weights"].append(list(map(float,line[2:-1])))
        layers[cLayer]["biases"].append(float(line[-1]))

for cLayer in range(len(layers)):  # stupid typing issues
    layers[cLayer]["weights"] = np.array(layers[cLayer]["weights"],dtype=np.float64)
    layers[cLayer]["biases"] = np.array(layers[cLayer]["biases"],dtype=np.float64)

with open(dataFile,"r") as dFile:  dataset = np.array([line.rstrip().split(',') for line in dFile])

newVals = list(enumerate(set(dataset[:,-1])))
dataCpy = np.copy(dataset)
for newVal,oldVal in newVals:  dataCpy[:,-1][dataCpy[:,-1] == oldVal] = newVal
dataset = dataCpy.astype(np.float64)  # stupid typing
dataset = (dataset-dataset.min(0)) / dataset.ptp(0)  # normalize
dataset[:,-1] *= (len(newVals)-1)

dataset = (dataset-dataset.min(0)) / (dataset.ptp(0))  # normalize
labels = np.identity(len(newVals))  # one-hot
dataset[:,-1] *= (len(newVals)-1)

trainData = dataset[lowTrain:hiTrain]
testData = dataset[lowTest:hiTest]

np.set_printoptions(precision=4)
print()
if intrnlFlag:
    for layerNo,layer in enumerate(layers):
        for b,w in zip(layer["biases"],layer["weights"]):  print("bias: {}    weights: {}".format(b,w))
        print()
print()

for epoch in range(nEpochs):
    for index,row in enumerate(trainData):
        inVectr = row[:-1]
        dsrdOut = labels[int(row[-1])]
        lyrOut = neuronOut(layers,inVectr)
        actlOut = lyrOut[-1]
        dVals = np.multiply(actlOut-np.square(actlOut),dsrdOut-actlOut)[...,None]
        inputs = lyrOut[-2][None,...]
        layers[-1]["weights"]+=dVals.dot(inputs)

        # back-prop
        for layerNo in reversed(range(-len(layers),-1)):
            nxtWghts = layers[layerNo+1]["weights"]
            curOuts = lyrOut[layerNo][...,None]
            dVals = np.multiply(curOuts-np.square(curOuts),nxtWghts.T.dot(dVals))
            if layerNo == -len(layers):  inputs = inVectr
            else:  inputs = lyrOut[layerNo-1]
            layers[layerNo]["weights"]+=dVals.dot(inputs[None,...])
    if epoch%10 == 0:
        nCorrct,ttlTests = nnIsRight(layers,testData)
        print("{:>6}{:>6} of {:>3}  {:.4}".format(epoch,nCorrct,ttlTests,nCorrct/ttlTests))

if intrnlFlag:
    print("\n")
    for layerNo,layer in enumerate(layers):
        for b,w in zip(layer["biases"],layer["weights"]):  print("bias: {}    weights: {}".format(b,w))
        print()

nCorrct,ttlTests = nnIsRight(layers,testData)
print("test result: {:>4} of {:>3}  {:.4}\n".format(nCorrct,ttlTests,nCorrct/ttlTests))

