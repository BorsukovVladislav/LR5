#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':

    n = int(input("Мой возраст: "))

    if n <= 100:
        print("Error")
    elif n % 10 == 1 and (n % 100) // 10 != 1:
        print(f"Мне {n} год")
    elif 2 <= n % 10 <= 4 and (n % 100) // 10 != 1:
        print(f"Мне {n} года")
    else:
        print(f"Мне {n} лет")
