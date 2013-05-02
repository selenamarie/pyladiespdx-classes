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



# List comprehensions: a concise way to make lists!
# The same loop, expressed as a List comprehension

eees = [ element for element in mylist if 'e' in element ]
print eees


# Generator expression -- Lazy evaluation!

eees = ( element for element in mylist if 'e' in element )
print eees

for e in eees:
    print e


# Some resources:
# http://www.secnetix.de/olli/Python/list_comprehensions.hawk
# http://stackoverflow.com/questions/2436607/how-to-use-re-match-objects-in-a-list-comprehension
# http://docs.python.org/2/tutorial/datastructures.html#list-comprehensions

