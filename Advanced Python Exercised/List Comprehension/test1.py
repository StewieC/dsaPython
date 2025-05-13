# list comprehension is a way to create list using coincise syntax
# it allows us to generate a new list by applying an expression to each utom in an existing iterable

# could be handy in writing clean and reusable code

x = [100, 2, 3, 4, 5]

res = [val ** 3 for val in x]

print(res)

# syntax of list comprehension
# [ EXPRESSION for ITEM in ITERABLE if CONDITION ]
"""
expression: The transformation or value to be included in the new list.

item: The current element taken from the iterable.

iterable: A sequence or collection (e.g., list, tuple, set).

if condition (optional): A filtering condition that decides whether the current item should be included.
"""