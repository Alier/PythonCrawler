import math

def make_visible(orig_func):
    def visible_math(*args):
        print '%s() was called with %r' % (orig_func.__name__,args)
        answer = orig_func(*args)
        print 'the answer is %r' % answer
        return answer
    return visible_math

def cache(orig_func):
    cached_answers = {}
    
    def inner(x):
        'Simulate slow labor intensive function'
        if x in cached_answers:
            return cached_answers[x]

        answer = orig_func(x)
        cached_answers[x] = answer
        return answer
    return inner

dispatch = {}

def register(short_name):
    def inner(func):
        dispatch[short_name] = func
        return func
    return inner

def interpreter():
    program = raw_input('Enter a program:')
    fields = program.split()
    x = int(fields[0])
    commands = fields[1:]
    print x,
    for command in commands:
        x = dispatch[command](x)
        print '--(%s)--> %s' % (command, x),
    print
    
##########################################################################

import time

@make_visible
@register('sq')
def square(x):
    'Compute a value times itself'
    return x * x

@make_visible
@register('cu')
def cube(x):
    'Compute a value times itself thrice'
    return x ** 3

@make_visible
@register('co')
def collatz(x):
    return 3*x+1 if x%2==1 else x//2

@cache                  # the sequence of cache and make_visible makes difference
@make_visible
@register('bg')
def big_func(x):
    'Simulate slow labor intensive function'
    print 'Doing hard work'
    time.sleep(1)
    return x + 1
