# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 08:39:47 2023

@author: shafi.muhammad
"""

lst0 = [0]*4
print("lst0= ",lst0)
print()
print("Modification de la liste.")
lst0[1] = 55; lst0[-1]=66; lst0[-2] = 77
print("lst0 = ",lst0)
print("lst0[len(lst0)-1] = ", lst0[len(lst0)-1])
print()
print("lst0[len(lst0)-2] = ",lst0[len(lst0)-2])

print("Création de liste 1D par comprehention.")
print()

lst1 = [0 for i in range(10)]
print(lst1)

print()

lst2 = [i for i in range(10)]
print(lst2)

print()

lst2[8] = 68
print(lst2)

print()

lst3 = [2*i for i in range(10)]
print(lst3)
print()

lst4 = [i for i in lst2 if i%2==0]
print(lst4)
print()

lst5 = [i for i in lst2 if i%2 != 0]
print(lst5)