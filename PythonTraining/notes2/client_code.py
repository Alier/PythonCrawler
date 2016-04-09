"Show-off circuitious from a user\'s point of view"

from __future__ import division
from circuitous import Circle

c = Circle(10)
print u'Tutorial for Circuitous\N{trade mark sign}'
print 'Using Circle version %d.%d' % Circle.version[:2]
print 'A circle with a radius of', c.radius
print 'has an area of', c.area()
print

## Academic Friends ##################################################

from random import random, seed
from pprint import pprint

n = 10000
jenny = 8675309
print 'DARPA Grant Proposal'
print 'to study the average area of circles'
print 'using Circuitous version %d.%d' % Circle.version[:2]
print 'preliminary study using %d random circles' % n
print "seeded using Jenny's number:", jenny
seed(jenny)
circles = [Circle(random()) for i in xrange(n)]
areas = [circle.area() for circle in circles]
average_area = sum(areas) / n
print 'The average area is %.5f' % average_area
print

## Rubber Sheet Company  #############################################

cut_template = [0.1, 0.2, 0.7]
print 'Spec sheet for the cut template:', cut_template
circles = [Circle(cut_radius) for cut_radius in cut_template]
for i, circle in enumerate(circles, 1):
    print 'Circle #%d' % i
    print 'A rubber circle with a cut radius of', circle.radius
    print 'has a perimeter of', circle.perimeter()
    print 'and a cold area of', circle.area()
    circle.radius *= 1.1          # circle.set_radius(circle.get_radius() * 1.1)
    print 'and a warm area of', circle.area()
    print

## National Tire Chain  ##############################################

class Tire(Circle):
    'Circle analytics specialed for tires'

    RUBBER_RATIO = 1.25

    def perimeter(self):
        'Perimeter corrected for the rubber on a tire'
        return Circle.perimeter(self) * self.RUBBER_RATIO     # Extending a method  <-- The parent gets called and the results are modified
        return 2.0 * 3.14 * self.radius * self.RUBBER_RATIO   # Overriding a method <-- The parent doesn't get called

    __perimeter = perimeter

class MonsterTire(Tire):

    RUBBER_RATIO = 1.50

t = Tire(30)
print 'A tire with an inner radius of', t.radius
print 'has an inner area of', t.area()
print 'and an odometer corrected outer perimeter of', t.perimeter()
print

m = MonsterTire(30)
print 'A monster tire has an odometer corrected outer perimeter of', m.perimeter()
print

## National Trucking Company #########################################

print u'An inclinometer reading of 5\N{degree sign}',
print 'is a %.1f%% grade.' % Circle.angle_to_grade(5)
print

## National Graphics Company #########################################

c = Circle.from_bbd(25)
print 'A circle with a bounding box diagonal of 25'
print 'has a radius of', c.radius
print 'an area of', c.area()
print 'and perimeter of', c.perimeter()
print

# ISO 10666:   No circle software shall use an area() method that
# accesses instance variables. It MUST call perimeter and infer
# the radius indirectly.

# ISO 10667:   No circle software shall store the radius.
# It MUST store the diameter and only the diameter.
