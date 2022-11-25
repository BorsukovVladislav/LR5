#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

if __name__ == '__main__':

    for N in range(100, 1000):
        num1 = N // 100
        num2 = (N % 100) // 10
        num3 = N % 10

        if num1 + num2 + num3 == num1 * num2 * num3:
            print(N)
