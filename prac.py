import pandas as pd
import numpy as np
import petl as pt
from petl import filldown,fillright,fillleft,look
from petl import unflatten

input = ['A', 3, True, None, 7, False, 'B', 2, False, 'C', 9]
table = unflatten(input, 3)
print(table)

a=filldown(table)
print(a)