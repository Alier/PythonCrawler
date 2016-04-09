from itertools import izip, izip_longest, chain, repeat

names = 'raymond rachel matthew'.split()
colors = 'red blue yellow green'.split()
cities = 'austin dallas chicago austin dallas austin chicago'.split()

print 'Task 1:  show the colors in uppercase'
for i in range(len(colors)):
    print colors[i].upper()

for color in colors:
    print color.upper()

print 'Task 2:  show the names and the position of each name in the list'
for i in range(len(names)):
    print '%d -> %s' % (i+1, names[i])

for i, name in enumerate(names, 1):
    print '%d -> %s' % (i, name)

print 'Task 3:  show the colors in reverse order'
for i in range(len(colors)-1, -1, -1):
    print colors[i]

for color in reversed(colors):
    print color

print 'Task 4:  display the names with the corresponding colors, ignoring mismatches'
n = len(names) if len(names) < len(colors) else len(colors)
for i in range(n):
    print '%s -> %s' % (names[i], colors[i])

n = min(len(names), len(colors))
for i in range(n):
    print '%s -> %s' % (names[i], colors[i])

for name, color in zip(names, colors):
    print '%s -> %s' % (name, color)

for name, color in izip(names, colors):
    print '%s -> %s' % (name, color)

for name, color in izip_longest(names, colors, fillvalue='unknown'):
    print '%s -> %s' % (name, color)

print 'Task 5:  Show the colors alphabetically'
for color in sorted(colors):
    print color.title()

print 'Task 6:  Show the colors ordered by the length of the colors'
deco = [(len(color), color) for color in colors]
print [color for size, color in deco]

print sorted(colors, key=len)

print 'Task 7:  Show the colors ordered by the next to last letter of the color'
print sorted(colors, key=lambda s: s[-2])

print 'Task 8:  Show the cities without duplicates'
# SELECT DISTINCT city FROM Cities ORDER BY city'
for city in sorted(set(cities)):
    print city.upper()

# set is an O(n) operation
# sorted is at worst O(n log n) however the TimSort typically
# does much better, occassionally approaching O(n)


