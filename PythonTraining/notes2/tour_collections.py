from collections import Counter, OrderedDict, deque
from itertools import imap
from pprint import pprint
import re

names = ''' tom david raymond rachel matthew susan timothy beatrice
brandon martin darlene daily randal suzy bryce mary rodney davin
bill dave'''.split()

people = 'raymond rachel matthew'.split()
foods = 'steak kale chocolate'.split()
colors = 'red green blue green red purple blue red green red'.split()

# Counting ##########################################################

c = Counter(colors)
print c.most_common(2)

with open('notes2/hamlet.txt') as f:
    play = f.read()

pprint(Counter(play.lower()).most_common(10))

words = re.findall(r"[a-z\'\-]+", play.lower())
pprint(Counter(words).most_common(10))

# OrderedDict is a kind of dict that remembers insertion order.
# It isn't the default because it takes a little more space
# to remember the order and it is a little slower.  Most use cases
# for dicts don't need order.  Main use cases are XML input and JSON
# input or Content Headers that are modified are rewritten out.
    
pref = OrderedDict()
for person, food in zip(people, foods):
    pref[person] = food
print pref

# Defaultdicts work like regular dicts, but if a key missing they call
# a factory function of zero arity and insert the new value.
# Principal use case is grouping:     d[feature] = list_of_elements_with_that_feature

print 'Group the names by the first letter of the name'
d = defaultdict(list)
for name in names:
    feature = name[0]
    d[feature].append(name)
pprint(dict(d))

print '\nGroup the names by the last letter of the name'
d = defaultdict(list)
for name in names:
    feature = name[-1]
    d[feature].append(name)
pprint(dict(d))

print '\nGroup the names by the length of the name'
d = defaultdict(list)
for name in names:
    feature = len(name)
    d[feature].append(name)
pprint(dict(d))

print '\nGroup the names by the number of vowels:  aeiouy'
d = defaultdict(list)
for name in names:
    feature = sum(imap(name.count, 'aeiouy'))
    d[feature].append(name)
pprint(dict(d))

# FIFO queues
# Deque is pronounced "DECK" and is short for double-ended queue
# Deque are designed for fast O(1) appends and pops at either end
disney_line = deque(names[:5])
print disney_line.popleft(), 'gets on the ride'
print disney_line.popleft(), 'gets on the ride'
print disney_line.popleft(), 'gets on the ride'
disney_line.append('mary')
disney_line.append('marge')
print disney_line.popleft(), 'gets on the ride'
print disney_line.popleft(), 'gets on the ride'
print disney_line.popleft(), 'gets on the ride'


