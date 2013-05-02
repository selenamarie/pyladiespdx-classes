#!/usr/bin/env python

mylist = [ 'one', 'two', 'three', 'four', 'five' ]
for element in mylist:
    print element







# For loop version
eees = []
for element in mylist:
    if 'e' in element:
        eees.append(element)

print eees





# As a List comprehension

eees = [ element for element in mylist if 'e' in element ]
print eees


# Generator expression -- Lazy evaluation!
eees = ( element for element in mylist if 'e' in element )

print eees

for e in eees:
    print e



