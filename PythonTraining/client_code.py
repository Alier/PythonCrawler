"Show-off circuitious from a user's point of view"

from __future__ import division  #Python 2.7 bug with /(int)
from circuitous import Circle

c = Circle(10)
print u'Tutorial for Circuitous\N{trade mark sign}'
print 'Using Circle Version %d.%d' % Circle.version[:2]
print 'A circle with a radius of', c.radius
print 'has an area of',c.area()
print

## Acadmic Friends ###########################################

from random import random, seed
from pprint import pprint

n = 10
jenny = 8675309

print 'DARPA Grant Proposal'
print 'to study the average area of circles'
print 'using Circuitous version %d.%d' % Circle.version[:2]
print 'preliminary study using %d random circles' % n
print "seeded using Jenny's number:",jenny
seed(jenny)
circles = [Circle(random()) for i in xrange(n)]
#pprint(circles)
areas = [circle.area() for circle in circles]
#pprint(areas)
#areas2 = map(circle.area, circles)
#pprint(areas2)

average_area = sum(areas)/n
print 'The average area is %.1f'% average_area
print

