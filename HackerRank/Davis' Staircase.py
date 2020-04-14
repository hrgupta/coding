'''
Solution to problem: Recursion: Davis' Staircase

You can find the description of the problem below:

https://www.hackerrank.com/challenges/ctci-recursive-staircase/problem
'''
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the stepPerms function below.
def stepPerms(n, d):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    elif n in d:
        return d.get(n)
    result = stepPerms(n - 1, d) + stepPerms(n - 2, d) + stepPerms(n - 3, d)
    d[n] = result
    return result

if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    s = int(input())

    d = {}

    for s_itr in range(s):
        n = int(input())

        res = stepPerms(n, d)

        fptr.write(str(res) + "\n")

    fptr.close()
