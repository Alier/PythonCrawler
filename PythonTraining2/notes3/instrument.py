''' Goals:

- Learn to instrument Python for performance analysis
- Practice subclassing subclassing builtin types
- Review the dunder methods from three-way compares, rich comparisons, and hashes
- Solidify knowledge of how containers work
- Practice with map() and filter()

'''

import math
from bisect import bisect

def reset():
    global cmp_cnt, hash_cnt
    cmp_cnt = 0
    hash_cnt = 0

def show():
    print '%d comparisons and %d hashes\n' % (cmp_cnt, hash_cnt)

class Int(int):
    'Instrumented tracer version of int'

    def __cmp__(self, other):
        global cmp_cnt
        cmp_cnt += 1
        print 'Comparing %r to %r' % (self, other)
        return int.__cmp__(self, other)

    def __hash__(self):
        global hash_cnt
        hash_cnt += 1
        print 'Hashing %r' % self
        return int.__hash__(self)

s = map(Int, [10, 20, 30, 50, 20, 5, 10, 15, 20])
a = Int(111)
b = Int(20)
c = Int(5)
d = c
e = s[3]

# Study list searches ##############################################

reset(); print a in s; show()            # Linear search, left-to-right.  When there is no match, takes len(s) comparisons
reset(); print b in s; show()            # Linear search has an early-out for matches.
reset(); print e in s; show()            # Identity implies equality, saving exactly one test.

print 'Expected sort cost:', len(s) * math.log(len(s), 2)
reset(); s.sort(); show()                # Sorts of random data take O(n log n) compares, but most data will run closer to O(n) because of partial ordering
reset(); bisect(s, a); show()            # Bisecting searchs are O(log n)
reset(); bisect(s, b); show()
reset(); bisect(s, e); show()
reset(); bisect(s, Int(19)); show()      # Primary use case for bisecting is searching ranges

# Study set searches ##############################################

s = map(Int, [10, 20, 30, 50, 20, 5, 10, 15, 20])
a = Int(111)
b = Int(20)
c = Int(5)
d = c
e = s[3]

other_intdata = [20, 30, 40, 300, 400, 500, 300, 400]
otherdata = map(Int, other_intdata) + s[-4:]
odata = set(otherdata)

reset(); s = set(s); show()              # Cost in len(s) hashes and 1 comparison per duplicate
reset(); print a in s; show()            # Cost of a missing lookup is a single hash with NO comparisons
reset(); print b in s; show()            # Cost of a match is 1 hash and 1 compare
reset(); print e in s; show()            # Cost of an exact match is a single hash with NO comparisons

print 'Using sets is MUCH cheaper than making them'
reset(); dict.fromkeys(s); show()        # Set-to-dict operations take no compares and no hashes
reset(); print s & odata; show()         # Intersection does NO hashes and compares only for non-identical overlaps
reset(); print s | odata; show()         # Union does NO hashes and compares only for non-identical overlaps
reset(); print s - odata; show()         # Difference does NO hashes and compares only for non-identical overlaps