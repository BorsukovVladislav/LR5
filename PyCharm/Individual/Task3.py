#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

if __name__ == '__main__':

    for n in range(100, 1000):
        num1 = n // 100
        num2 = (n % 100) // 10
        num3 = n % 10

        if num1 + num2 + num3 == num1 * num2 * num3:
            print(n)
