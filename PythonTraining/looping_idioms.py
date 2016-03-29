from itertools import *

names = 'raymond rachel matthew'.split()
colors = 'red yellow blue green'.split()
cities = 'austin dallas chicago austin dallas austin chicago'.split()

print 'Task 1: show the colors in uppercase'
# for i in range(len(colors)):
# 	print colors[i].upper()
# 	
for color in colors:
	print color.upper()
	
print 'Task 2: show the names and the positions of each name in the list'
for i in range(len(names)):
	print '%d -> %s' % (i+1, names[i])

for i, name in enumerate(names, 1):
        print '%d -> %s' % (i,name)
        
print 'Task 3: show the colors in reverse order'
for i in range(len(colors)-1, -1, -1):
        print colors[i]

for color in reversed(colors):
        print color

print 'Task 4: display the names with the corresponding color'
# Algor derivatives: Ternary operator or conditional expression
# (cond) ? positiveres : negativeres;
# result = (score >= 70) ? "pass":"fail";
# Python way:
#       posres if cond else negres
# example: 
#>>> score = 55
#>>> 'pass' if score >= 70 else 'fail'
#'fail'
n = len(names) if len(names) < len(colors) else len(colors)
for i in range(n):
        print '%s -> %s' % (name[i], colors[i])

# better way to use reducer
n = min(len(names),len(colors))
for i in range(n):
        print '%s -> %s' % (name[i], colors[i])

# best way and preferred way, zip(x,y) throws away the last few elements
# problem with zip it doesn't make iterator
for name, color in zip(names, colors):
        print '%s -> %s' % (name, color)

# izip creates an interator
for name, color in izip(names, colors):
        print '%s -> %s' % (name, color)

for name, color in izip_longest(names, colors, fillvalue = 'unknown'):
        print '%s -> %s' % (name, color)

print 'Task 5: Show the colors alphabetically'
for color in sorted(colors):
        print color

#DSU -> Decorate-Sort-Undecorate Schwartzian Transform

print 'Task 6: Show the colors by the length of the color'
# method 1
deco = [(len(color), color) for color in colors]
deco.sort()
print [color for size, color in deco]

# method 2
print sorted(colors, key = len)

print 'Task 7: Show the colors by the order of the last letter of the color'
print sorted(colors, key = lambda s:s[-2])

print 'Task 8: Show the cities without duplicates'
# set is an o(n) operation
# sorted is at worst O(n log n) however the TimSort typically
# does much better, occassionally reach O(n)
for city in sorted(set(cities)):
        print city.upper()
