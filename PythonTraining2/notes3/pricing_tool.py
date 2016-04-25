from __future__ import division

from validators import OneOf

class PriceRange(object):

    kind = OneOf('stock', 'bond', 'option')
    symbol = OneOf('CSCO', 'HP', 'BOA', 'WLP', 'GOOG')

    def __init__(self, kind, symbol, low, high):
        self.kind = kind
        self.symbol = symbol
        self.low = low
        self.high = high

    @property
    def midpoint(self):
        return (self.low + self.high) / 2

portfolio = [
    PriceRange('stock', 'CSCO', 24, 31.50),
    PriceRange('stock', 'HP', 45, 51),
    PriceRange('bond', 'BOA', 32, 46),
    PriceRange('option', 'BOA', 'hello', 18),
    PriceRange('option', 'WLP', 14, -27),
]


    
