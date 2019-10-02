#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 13:33:32 2019

@author: danilalobar
"""

from operator import add
res = 0
for x in range(10,30,2):
    res+= (pow(x,2)+3)
    print(res)