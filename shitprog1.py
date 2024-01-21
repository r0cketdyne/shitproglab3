#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 20:37:40 2024

@author: stephenson
"""

sal = 50000

sales = (int(input("how much did you make at actual sales?" )))
if sales >= 100000:
    bonsales = sales * 0.0125
    print(bonsales +sal)
else:
   print("your're taking home", sal , "at Tc")
