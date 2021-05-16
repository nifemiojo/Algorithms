#!/bin/python3

import math
import os
import random
import re
import sys

# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER d
#
def rotLeft(original, d):
    rotated = original.copy()

    for i in range(len(original)):
        rotated[i-d] = original[i]
    return rotated


if __name__ == '__main__':
    result = rotLeft([1, 2, 3, 4], 3)
    print(result)
