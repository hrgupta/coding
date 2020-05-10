'''
Solution to problem: Counting Valleys

You can find the description of the problem below:

https://www.hackerrank.com/challenges/counting-valleys/problem
'''
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    valleys = 0
    sea_level = 0
    for i in range(n):
        if(s[i]=='U'):
            sea_level+=1
        else:
            if(sea_level==0):
                sea_level-=1
                valleys+=1
            else:
                sea_level-=1
    return valleys

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
