'''

Most important skills is how turn them off or all one:

    $ python -W ignore warnings_demo.py
    $ python -W always warnings_demo.py

Concept map for warnings:
-------------------------
* Policies are called "actions":  error, ignore, always, once, default (once per module)
* Filter are tools that apply policies to selected warnings
  - "Messages" are the text that goes with warning.  You can match on a regex
  - "Category" is the warning classes:  UserWarning, DeprecationWarning, RuntimeWarning
  - "Module" is where the warning happened.
  - "Line number" is used to shut-off a specific warning

'''

import warnings
import math

class RaymondWarning(UserWarning):
    'You can define your own warning categories'

def sqrt(x):
    if x >= 0.0:
        return math.sqrt(x)
    warnings.warn('Taking the square root of a negative number')
    return math.sqrt(-x) * 1j

def user(x):
    warnings.warn('The "user" function is deprecated, use "sqrt" instead', DeprecationWarning)
    return sqrt(x ** 3.0)

#warnings.filterwarnings('always', '.*square root.*')
#warnings.filterwarnings('once', category=DeprecationWarning)

print user(5)
print user(-5)
warnings.warn('Oops, I did it again.  I played with heart, ...')
print user(6)
warnings.warn('Python is the best!', RaymondWarning)
print user(-6)
print 'Done'
