''' Goal: Become a black belt with properties

Fundamental action: Converts attribute lookup like a.x into method access like a.m()

Mechanisms: it reprograms the dot, but it can only be done in new-style classes.

Computed fields using properties:
* Saves storage space
* Reduces risk of data inconsistency
* Provide a clean consistent API for users

Managed attributes:
* Control all read and write access to an attribute
* A primary use is validating data at the time it is store
* This is a fantastic debugging technique for tracking down hard-to-find data corruption bugs

It is common to have a module full of validators:
* validate_percentage
* validate_between(low=500, high=1000)
* validate_email
* validate_url
* validate_str(minsize=3, maxsize=5, predicate=str.isupper)
* validate_one_of('stock', 'bond', 'option', 'currency','future')

'''

from __future__ import division             # to surpress the integer division bug 
from validators import validate_percentage

class PriceRange(object):
    def __init__(self, symbol, low, high):
        self.symbol = symbol
        self.low = low
        self.high = high

    # Computed fields
    @property    #equal to : midpoint = property(midpoint)
    def midpoint(self):
        return (self.low + self.high) / 2
    
    def __repr__(self):
        return '%s(symbol=%r, low=%r, high=%r)' %\
               (self.__class__.__name__, self.symbol, self.low, self.high)

    # Managed attributes
    
    @property  #getter can use this
    def low(self):      #low = property(get_low, set_low) 
        return self._low

    @low.setter         #low = property(get_low, set_low) 
    def low(self,low):
        validate_percentage(low)
        self._low = low

    #low = property(get_low, set_low)  #can take 4 parameters: getter, setter, deleter, '''string

    # Managed attributes
    @property           #high = property(get_high, set_high)
    def high(self):
        return self._high

    @high.setter        #high = property(get_high, set_high)            
    def high(self,high):
        validate_percentage(high)
        self._high = high
    
p = PriceRange('CSCO',25,32)

