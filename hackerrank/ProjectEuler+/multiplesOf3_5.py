#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    nums = 0
    for i in range(n):
        if i%3==0:
            nums+=i 
        elif i%5==0:
            nums+=i 

    print(nums)

    """
    TOO MUCH TIME COMPLEX 
    GOT TO OPTIMIZE!!!!
    """