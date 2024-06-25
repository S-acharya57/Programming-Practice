#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'matchingStrings' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY stringList
#  2. STRING_ARRAY queries
#

def matchingStrings(stringList, queries):
    arr2 = []
    # Write your code here
    for i, str_ in enumerate(queries):
        if str_ in stringList:
            arr2.append(stringList.count(str_))
            # print(f'{arr2} is the new value!')
        else:
            arr2.append(0)

        # print('Arr2 is', arr2)
    return arr2 

stringList_count = int(input().strip())

stringList = []

for _ in range(stringList_count):
    stringList_item = input()
    stringList.append(stringList_item)

queries_count = int(input().strip())

queries = []

for _ in range(queries_count):
    queries_item = input()
    queries.append(queries_item)

res = matchingStrings(stringList, queries)
print(res)
