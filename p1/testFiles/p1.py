#!/usr/bin/env python3
import numpy as np
import sys
from math import exp

# Function to determine if a string can be converted to a number
def is_number(test_string):
    try:
        float(test_string)
        return True
    except:
        return False
def parse_line(line):
    # Get rid of comments
    comment_pos = line.find("#")
    if comment_pos != -1:
        line = line[:comment_pos]
    neuron = list(filter(is_number, line.split(" ")))
    return (int(neuron[0]), int(neuron[1]), list(map(float, neuron[2:-1])), float(neuron[-1]))
def parse_input(line):
    # Get rid of comments
    comment_pos = line.find("#")
    if comment_pos != -1:
        line = line[:comment_pos]
    return list(map(float, filter(is_number, line.split(" "))))

with open(sys.argv[1],"r") as input_file:
    # Strip off newlines
    lines = map(str.rstrip, input_file.readlines())
    # Filter out comments and empty lines
    lines = list(filter(lambda line: line != "" and not line.startswith("#"), lines))
    # Parse remaining (neuron) lines
    neurons = list(map(parse_line, lines[:-1]))
    # Get input line
    input_vector = parse_input(lines[-1])

sigmoid = lambda x: 1 / (1 + np.exp(-x))

layers = []
biases = []
cur_layer = -1
for neuron in neurons:
    if neuron[0] > cur_layer:
        cur_layer = neuron[0]
        layers.append([])
        biases.append([])
    layers[-1].append(neuron[2])
    biases[-1].append(neuron[3])


transformed_vector = np.array([input_vector])
for layer, bias in zip(layers, biases):
    transformed_vector = sigmoid(np.dot(transformed_vector, np.array(layer).T) + np.array(bias))

print(' '.join(map(str, transformed_vector[0])))
