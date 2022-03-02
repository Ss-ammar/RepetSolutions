# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 12:04:45 2022

@author: MyLaptop
"""

import numpy as np
import math
from math import sin, exp
from scipy.optimize import minimize_scalar

def objective_function(x): 
    return (sin(x-2) ** 2) * exp((-x) ** 3) 
    #when I change the sign of the function -f(x) I got this error:
        #OverflowError: math range error
result = minimize_scalar(objective_function)

print(result)
     
    