'''Rule:  If you ever override __eq__ to create a new equivalence class
          be sure to update __hash__ as well to keep them in-sync
          so that x==y implies hash(x)==hash(y).

          If you don't, then sets and dicts are broken and equivalents items before unfindable

'''

s = [10, 5, 18, 27, 30, 41, 12, 39, 7]

even_odd = [[10, 18, 30, 12], [5, 27, 41, 39, 7]]

x = 39.0
print x in even_odd[int(x) % 2]

# Required homomorphism for hash tables to work:
#   x == y    |->    hash(x) == hash(y)
#  39 == 39.0 |->  int(39)%2 == int(39.0)%2

class Str(str):
    'Make strings that do case-insensitive comparisons'
    
    def __eq__(self, other):
        return self.lower() == other.lower()
    
    def __hash__(self):
        return hash(self.lower())

print set(map(Str, 'Raymond rachel MATTHEW raymond RACHEL Matthew'.split()))

print "April Fools Joke.  Don't do this for real"

import random

class Int(int):
    def __hash__(self):
        return random.randrange(100000)

data = map(Int, [10, 20, 30, 40, 30, 20, 10])
print set(data)
