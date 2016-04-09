''' Monkey patching is making variable assignments into some other namespace.

When monkey patching occurs, there is always something wrong.
But the monkey patch is the fix, not the problem.

Legitimate use cases:
  * Fix an erroneous constant
  * Improve error messages
  * Making functions more robust (handling a broader range of inputs)

Illegitimate use cases:

  * If you monkey patch your own code, you're living in a state of sin
  * You should just fix the code directly.

'''

import algebra
import math

algebra.pi = math.pi                                # Monkey patch

original_area_triangle = algebra.area_triangle      # Step 1:  Save the original

def better_area_triangle(base, height):             # Step 2:  Write a wrapper to make the repair
    try:
        return original_area_triangle(base, height)
    except RuntimeError:
        raise ValueError('Illegal base and height.  No negatives allowed')

algebra.area_triangle = better_area_triangle        # Step 3:  Monkey patch the wrapper back into algebra

original_sqrt = math.sqrt                           # Step 1:  Save the original

def better_sqrt(x):                                 # Step 2:  Write a wrapper to make the repair
    'Wrap math.sqrt() to add support for negative inputs'
    if x >= 0.0:
        return original_sqrt(x)
    return original_sqrt(-x) * 1j

math.sqrt = better_sqrt                             # Step 3:  Monkey patch the wrapper back into algebra    


if __name__ == '__main__':
    print u'I have it on good authority that \N{greek small letter pi} is exactly:', algebra.pi
    print 'The area of a circle with radius 10 is:', algebra.area(10)
    try:
        print 'The area of the 1st triangle is:', algebra.area_triangle(5, 40)
        print 'The area of the 2nd triangle is:', algebra.area_triangle(5, -40)
    except ValueError:
        print 'Doh!  Sorry for the negative input'
    print 'Solution to 12x^2 + 23x + 10 is:',
    print algebra.quadratic(a=12, b=23, c=10)
    print 'Solution to 12x^2 + 8x + 10 is:'
    print algebra.quadratic(a=12, b=8, c=10)
    
    
