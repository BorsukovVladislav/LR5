#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

if __name__ == '__main__':

    a = int(input('Введите a: '))
    b = int(input('Введите b: '))
    c = int(input('Введите c: '))

    if math.fabs(a) >= 4:
        print(a)
    if math.fabs(b) >= 4:
        print(b)
    if math.fabs(c) >= 4:
        print(c)
