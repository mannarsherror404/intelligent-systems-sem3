# -*- coding: utf-8 -*-
"""Experiment 8 IS-1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/144hR0Gn4A2H5MP31-kH68q4DURiFXioE

#EXPERIMENT EIGHT

## 🔬 Experiment : Constraint Satisfaction Problem

Implement a Constraint Satisfaction Problem (CSP) in Python for the following:

Part A – Without Using Constraint Module:

Find all (x, y) where x ∈ {1, 2, 3}, and 0 <= y < 10, and x + y >= 5.
"""

# CSP Implementation Without Using Constraint Module

valid_pairs = []

for x in [1, 2, 3]:
    for y in range(10):
        if x + y >= 5:
            valid_pairs.append((x, y))

print("Valid (x, y) pairs where x + y >= 5:")
print(valid_pairs)

# Install the constraint module (only needs to be run once)
!pip install python-constraint

# CSP Implementation Using Constraint Module
from constraint import Problem

problem = Problem()

# Define the variables and their domains
problem.addVariable("x", [1, 2, 3])
problem.addVariable("y", list(range(10)))

# Define the constraint
problem.addConstraint(lambda x, y: x + y >= 5, ("x", "y"))

# Get solutions
solutions = problem.getSolutions()

print("Valid (x, y) pairs where x + y >= 5:")
print(solutions)