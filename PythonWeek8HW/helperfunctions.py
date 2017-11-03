
# coding: utf-8

# In[ ]:
from functools import reduce

def add(inList):
    return sum(inList)

def product(inList):
    return reduce(lambda x,y: x*y, inList)

def diff(inList):
    return reduce(lambda x,y: x-y, inList)

def greatest(inList):
    return max(inList)
