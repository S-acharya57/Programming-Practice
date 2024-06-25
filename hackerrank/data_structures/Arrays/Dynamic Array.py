#!/bin/python3

import math
import os
import random
import re
import sys
#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):
    # print(f'Queries is {queries}')
    # Write your code here
    arr = [[1000] for i in range(n)]
    print(f'Basic arr: {arr}')
    lastAnswer = 0 
    answers = []
    i = -1
    for query in queries:
        i = i+1
        # print(f'\n\t\t{i}, Query is {query}')
        # print(f')
        # print(f'\n\tDeciding Number -> {query[0]}')
        if query[0] ==1:
            
            idx = ((query[1]^lastAnswer)% n)
            print(f'idx is achieved as {idx}')
            # print(f'x is {query[1]}\tidxx is {idx}')
            if (arr[idx][0] == 1000):
                 arr[idx] = [(query[2])]
            else:
                arr[idx].append(query[2])
            print(f'Arr has appened it as {arr}')
        else:
            # print(f'Final answer {query[0]}  is lastAnswer') 
            # print(f'\t\tStart of 2, \n\t\t arr = {arr}')
            print(f'query[1]:{query[1]},\t')
            print(f'query[1]^lastAnswer:{query[1]^lastAnswer},\t')
            idx = ((query[1]^lastAnswer)% n)
            # print(f'x is {query[1]}\tidxx is {idx}')
            print(f'\tarr:{arr}')
            print(f'idx: {idx},\t arr[idx]:{arr[idx]},\tarr[idx][y]:{arr[idx][query[2]]},\tlen(arr[idx]) : {len(arr[idx])}')
            lastAnswer = arr[idx][query[2]%len(arr[idx])]
            print(f'last answer is {lastAnswer}')

            answers.append(lastAnswer)
    
    return answers 

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    # n is the size of arr to create
    n = int(first_multiple_input[0])

    # q is the number of queries

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    print(result)