''' Circuitous(tm)                                    # Give the project a name
An Advanced Circle Analytics                          # Elevator Pitch --> What problem you solve and how you're solving it
'''

# New-style classes inherit from object
# Inheritance is a tool for code re-use.  It allow one class to reuse the code from another.
# object() has a __getattribute__ method that provides a reprogrammable dot.
# Python programmers tend to document first.
# 1) It better defines the problem, making it more solvable.
# 2) There is an immediate payoff with help(), pydoc, sphinx, tooltip, etc.
# Give names to "magic constants".  Second benefit is making the value consistent in the module.
# D.R.Y. :  Do Not Repeat Yourself.  is a code smell.
#  ^--- There should be a SINGLE source of truth
# Code Smell:  Code that works but is awkward to understand or maintain
# Indicates a need to refactor
# Long existing convention in many languages is that constants have uppercase variable names
# M.V.P. -- Minimum Viable Product
# YAGNI,RT -- You ain't gonna need it right now
# "Code is your enemy"
# "Dogfooding" -- Eat you own dogfood --> Be your own first user.

import math                                 # The purpose of modules is for code organizaition and reuse
from collections import namedtuple

Version = namedtuple('Version', ['major', 'minor', 'micro'])

class Circle(object):
    'Advanced circle analytic toolkit'

    __slots__ = ['diameter']                # Implement the Flyweight Design Pattern, saving memory by eliminating the instance dictionaries

    version = Version(0, 10, 1)             # Class variables are SHARED by all instances and visible from the class

    # The use of "self" is a cultural norm
    # Parameter names are user visible, part of the API and should be spelled-out.
    # Spelling-out avoids cultural bias for abbreviations.  Networking IS a common culture.
    # When copying from one namespace to another, we generally keep the name the same.
    def __init__(self, radius):
        self.radius = radius                # Instances variables should be UNIQUE to each instance

    def area(self):                         # Regular methods take "self" as the first argument
        'Perform quadrature on a planar shape of uniform revolution'
        p = self.__perimeter()              # Class local reference, because sometimes you need "self" to really be you
        radius = p / 2.0 / math.pi
        return math.pi * radius ** 2.0

    def perimeter(self):
        'Compute the closed line integral for the locus of points equidistant from a given point'
        return 2.0 * math.pi * self.radius

    __perimeter = perimeter                 # Name mangling to automatically prepend the name of the class

    # Best practice for repr is to look like how the object COULD have been created
    # Don't assume that "self" means you; instead, it could be one of your children
    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.radius)

    @staticmethod                                   # Reprograms the dot to NOT add "self" as the first argument
    def angle_to_grade(angle):                      # Use case is attaching regular functions to classes to improve findability which is a human factors problem
        'Convert an inclinometer reading in degrees into a percent grade'
        return math.tan(math.radians(angle)) * 100.0

    @classmethod                                    # Reprograms the dot to add the class as the first argument
    def from_bbd(cls, bbd):                         # Use case alternative constructors
        'Construct a new circle from a bounding box diagonal'
        radius = bbd / 2.0 / math.sqrt(2.0)
        return cls(radius)

    @property
    def radius(self):
        return self.diameter / 2.0

    @radius.setter                                   # Reprograms the dot to convert attribute access like c.radius into method access like c.get_radius()
    def radius(self, radius):
        self.diameter = radius * 2.0

