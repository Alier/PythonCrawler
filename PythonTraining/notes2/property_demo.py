''' Goal:  Become a black belt with properties

Fundamental action:  Converts attribute lookup like a.x into method access like a.m()

Mechanism:  It reprograms the dot, but that can only be done in new-style classes.

Computed fields using properties:
* Saves storage space
* Reduces risk of data inconsistency
* Provide a clean, consistent API

Managed attributes:
* Control all read and write access to an attribute
* A primary use case is validating data at the time it is stored
* This is a fantastic debugging technique for tracking down
  hard-to-find data corruption bugs (like crickets at night).

It is common to have a module full of validators:
* validate_percentage
* validate_between(low=500, high=1000)
* validate_email
* validate_url
* validate_str(minsize=3, maxsize=5, predicate=str.isupper)
* validate_one_of('stock', 'bond', 'option', 'currency', 'future')

'''

from __future__ import division
from validators import validate_percentage

class PriceRange(object):
    
    def __init__(self, symbol, low, high):
        self.symbol = symbol
        self.low = low
        self.high = high

    @property                     # midpoint = property(midpoint)
    def midpoint(self):
        return (self.low + self.high) / 2    

    def __repr__(self):
        return '%s(symbol=%r, low=%r, high=%r)' % \
               (self.__class__.__name__, self.symbol, self.low, self.high)

    # Managed attributes

    @property
    def low(self):
        return self._low

    @low.setter                    # low = property(get_low, set_low)
    def low(self, low):
        validate_percentage(low)
        self._low = low

    @property
    def high(self):
        return self._high

    @high.setter
    def high(self, high):
        validate_percentage(high)
        self._high = high

p = PriceRange('CSCO', 25, 32)










