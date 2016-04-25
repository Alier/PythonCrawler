'Space-efficient probabalistic data structure'

#https://en.wikipedia.org/wiki/Bloom_filter

from random import seed, sample
from bitarray import BitArray

class BloomFilter:
    def __init__(self, iterable =(), population = 56, probes = 6):
        self.population = xrange(56)
        self.probes = probes
        self.data = BitArray(population)
        for name in iterable:
            self.add(name)

    def add(self, name):
        seed(name)
        lucky = sample(self.population, self.probes)
        for i in lucky:
            self.data[i] = 1 

    def __contains__(self, name):
        seed(name)
        lucky = sample(self.population, self.probes)
        return all(self.data[i] for i in lucky)   # all/any does KEEP the early exit feature and very efficient as it's c code
        
if __name__ == '__main__':
    
    family = 'raymond rachel matthew ramon gayle dennis sharon'.split()
    
    hettingers = BloomFilter(family)
    print 'matthew' in hettingers
    print 'bob' in hettingers

