#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import math

EPS = 1e-10

if __name__ == '__main__':

    x = float(input('Enter value of X: '))
    if x == 0:
        print('Illegal value of X', file=sys.stderr)
        exit(1)

    a = -3 * x ** 2 / 100
    Sum, n = a, 1

    while math.fabs(a) > EPS:
        a *= (-x ** 2 * (2 * n + 1)) / ((2 * n + 3) ** 2 * (2 * n + 2))
        Sum += a
        n += 1

    print(Sum)
