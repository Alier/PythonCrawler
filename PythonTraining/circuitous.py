''' Circuitous(tm)                              # Give the project a name
An Advanced Circle Analytics                    # Elevator Pitch -> What problem you solve and how you solve it
'''

# New-style classes inherit from object
# Inheritance is a tool for code re-use. It allows one class to reuse the code from another.
# object() has a __getattribute__ method that provides a reprogrammable dot.
# Python pgorammers tend to document first.
# 1) It better defines the problem, makeing it more solvable.
# 2) There is an immediate payoff with help(), pydoc, sphinx, tooltip, etc
# Give names to "magic constants". Second benefit is maing the value consistent in the module.
# D.R.Y. : Do not Repeat Yourself. is a code smell.
# Code Smell: Code that works but is awkward to understand or maintain
# Indicates a need to refactor
# Constants should have uppercase variable names
# M.V.P. -- Minimum Viable Product
# YANGI,RT -- You ain't gonna need it right now
# "Dogfooding" -- Eat your own dogfood --> Be your own first user.Alpha

import math
from collections import namedtuple

Version = namedtuple('Version',['major','minor','micro'])

class Circle(object):
    version = Version(0,1,5)       # Class variables are shared by all instance and visible 
    
    'Advanced circle analytic toolkit'
    # The use of "self" is a cultural norm
    # Parameter names are user visible, part of the API and should be spelled-out.
    # Spelling-out avoids cultural bias for abbreviations.
    # When copying from one namespace to another, we generaaly keep the name the same. 
    def __init__(self, radius):
        self.radius = radius

    def from_bbd(cls, bbd):         # Use case alternative constructors
        'Construct a new circle from a bounding box diagonal'
        radius = bbd / 2.0 / math.sqrt(2.0)
        return cls(radius)

    from_bbd = classmethod(from_bbd) #Reprograms the dot to add the class as the first argument
    
    def area(self):
        'Perform quadrature on a planar shape of uniform revolution'
        return math.pi * self.radius**2.0

    def perimeter(self):
        'Compute the closed line integral for the locus of points equidistant from a given point'
        return 2.0 * math.pi * self.radius
    
    def angle_to_grade(angle):              # Use case is attaching regular functions to classes to improve findability which is human factor problem that can't be programmed away
        'Convert an inclinometer reading in degrees into a percent grade'
        return math.tan(math.radians(angle)) * 100.0

    angle_to_grade = staticmethod(angle_to_grade) #Reprograms the dot to NOT add "self" as parameter

    # Best practice for repr is to look like how the object COULD have been created
    # %r is using __repr__
    # Don't assume self means you ,it could be one of your children
    def __repr__(self): 
        return '%s(%r)' % (self.__class__.__name__, self.radius)
