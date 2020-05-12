'''
Solution to problem: Counting Valleys

You can find the description of the problem below:

https://www.hackerrank.com/challenges/sock-merchant/problem
'''
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    dic = {}
    for i, num in enumerate(ar):
        if dic.get(num)!=None:
            dic[num] += 1
        else:
            dic[num] = 1
    pairs = 0
    for key, value in dic.items():
        if value > 1:
            pairs += int(value/2)
    return pairs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
