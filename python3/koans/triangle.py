#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Triangle Project Code.

# Triangle analyzes the lengths of the sides of a triangle
# (represented by a, b and c) and returns the type of triangle.
#
# It returns:
#   'equilateral'  if all sides are equal
#   'isosceles'    if exactly 2 sides are equal
#   'scalene'      if no sides are equal
#
# The tests for this method can be found in
#   about_triangle_project.py
# and
#   about_triangle_project_2.py
#
def triangle(a, b, c):
    angles = (a, b, c)
    if [a for a in angles if a <= 0]:
        raise TriangleError('All sides must be greater than 0.')
    if a + b < c or a + c < b or b + c < a:
        raise TriangleError('No two sides may be smaller than the third side.')
    if a is b and a is c:
        return 'equilateral'
    if a is b or a is c or b is c:
        return 'isosceles'
    return 'scalene'
# Error class used in part 2.  No need to change this code.
class TriangleError(Exception):
    pass
