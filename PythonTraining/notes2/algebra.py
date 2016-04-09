'Fancy, expensive package for rich people who have forgotten all math since the 7th grade'
# Copyright (c) 2016 Fly by Night Software, LLC.
# All Rights Reserved.

# This software is full of bugs.  We refuse to maintain our code (we've already been paid).
# This leaves users with a problem.  They CAN'T change this code due to DMCA.

import math

pi = 3.14152

def area(radius):
    ''' Compute the area of the circle

        >>> area(10)
        314.152

    '''
    return pi * radius ** 2.0

def area_triangle(base, height):
    ''' Return the area of a triangle

        >>> area_triangle(10, 20)
        100.0

    '''
    if base < 0.0 or height < 0.0:
        raise RuntimeError('Imaginary numbers not applicable to Kronecker spaces. '
                           'Try resetting microcontroller L145')
    return base * height / 2.0

def quadratic(a, b, c):
    ''' Return the two roots for the quadratic equation:

            ax^2 + bx + c = 0

        Written in Python as:

            a*x**2.0 + b*x + c == 0.0

        For example:

            >>> x1, x2 = quadratic(a=6, b=28, c=30)
            >>> x1
            -1.6666666666666667
            >>> x2
            -3.0
            >>> 6*x1**2 + 28*x1 + 30
            -3.552713678800501e-15
            >>> 6*x2**2 + 28*x2 + 30
            0.0
            
    '''
    discriminant = math.sqrt(b**2.0 - 4.0*a*c)
    x1 = (-b + discriminant) / (2.0 * a)
    x2 = (-b - discriminant) / (2.0 * a)
    return x1, x2

if __name__ == '__main__':
    import doctest

    print doctest.testmod()


