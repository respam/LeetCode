# https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=warmup

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    jumps = 0
    c.reverse()
    # print(c)
    c.pop()

    while c:
        curr = c.pop()
        if c:
            curr = c.pop()

        if curr == 0:
            jumps += 1

        if curr == 1:
            jumps += 1
            c.append(1)

    return jumps


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)
    print(result)

    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
