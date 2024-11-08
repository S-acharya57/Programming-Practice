#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def next_multiple(num):
    divisor_ = num//5 
    return (divisor_+1) * 5

def gradingStudents(grades):
    # Write your code here
    for grade in grades:
        next_ = next_multiple(grade)
        print(next_)
        if next_-grade<3:
            print(f'Returning next_ as {next_}')
            return str(next_)
        if grade<40:
            print(f'Returning grade as {grade}')
            return str(grade) 

if __name__ == '__main__':
    
    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    print('\n'.join(map(str, result)))
