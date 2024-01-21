#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 21:20:09 2024

@author: stephenson
"""

grade1 = 0
grade2 = 0
grade3 = 0

grade1 += int(input("what was your first test score noob."))
grade2 += int(input("what as your second test score nooblet"))
grade3 += int(input("what was your third score nub"))
avscore = ((grade1 + grade2 + grade3) / 3)
if avscore >= 70.0:
        print("u passed!")
else:
        print("Noooo...you failed!")
        