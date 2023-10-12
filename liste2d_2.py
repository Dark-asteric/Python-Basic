# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 08:29:06 2023

@author: shafi.muhammad
"""

lst = [[0,1,2,3,4],[10,11,12,13,14]]
print(lst)

# one method to access values in list

for i in range(len(lst)):
    for j in range(len(lst[i])):
        print(lst[i][j], end = " ")
    print()
print()

for it in lst:
    #print(it) # Print all values at same time.
    for it2 in it:
        print(f"values = {it2}",end=" ")
    print()