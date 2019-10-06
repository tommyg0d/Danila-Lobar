#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 14:47:54 2019

@author: danilalobar
"""

import random

l = ['самовар', 'весна', 'лето']

word = l[random.randint(0,len(l)-1)]
letter = random.randint(0,len(word)-1)
randByk = list(word)[letter]

randWord = list(word)
randWord[letter] = '?'
print(''.join(randWord))

a = input("Введите букву:  ")

if a == randByk:
        print('Победа!')
else: print('Увы! Попробуйте в другой раз.')
   