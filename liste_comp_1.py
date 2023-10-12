# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 08:56:22 2023

@author: shafi.muhammad
"""

# Create a list values are from 0 to 10:
    
lst0 = [0 for i in range(10)]
print(lst0)
print()

# Add 100 in 4th position :
    
lst0[3] = 100
print(lst0)

# Create another list from -2 to 8

lst1 = [i for i in range(-2,9,1)]
print(lst1)

# Add 80 in last position of the list :

lst1[len(lst1)-1] = 80
print(lst1)
print()

# Create another list, start from -10 to 21 and 4 steps ahead:

lst2 = [i for i in range(-10,21,4)]
print(lst1)
print()

# Add 44 in the first position :
    
lst2[0] = 44
print(lst2)

# Create another list and contain positive numbers from list 3:

lst3 = [i for i in lst2 if i>-1]
print(lst3)
print()


# assign to the first term of lst2 the value of the second term of lst0:

lst2[0] = lst0[1]
print(lst2)
print()

# Create another list and add negative values and odd numbers from lst2:

lst4 = [i for i in lst2 if (i<1 and i%2 !=0)]
print(lst4)
print()

# Create another list and add positive values and even numbers from lst2:
    
lst5 = [i for i in lst2 if (i>0 and i%2 ==0)]
print(lst5)
print()

# Reverse list:
l = [2,3,4,5,7,8]
ls = [l[-i-1] for i in range(len(l))]
print(ls)
