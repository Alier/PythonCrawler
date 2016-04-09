import math
from pprint import pprint

def make_visible(orig_func):
    def visible_math(*args):
        print '%s() was called with %r' % (orig_func.__name__, args)
        answer = orig_func(*args)
        print 'the answer is %r' % answer
        return answer
    return visible_math

dispatch = {}

def register(shortname):
    def inner(func):
        dispatch[shortname] = func
        return func
    return inner

def interpreter():
    program = raw_input('Enter a program: ')
    fields = program.split()
    x = int(fields[0])
    commands = fields[1:]
    print x,
    for command in commands:
        x = dispatch[command](x)
        print '--(%s)--> %s' % (command, x),
    print

def cache(orig_func):
    answers = {}
    def inner(x):
        if x in answers:
            return answers[x]
        answer = orig_func(x)
        answers[x] = answer
        return answer
    return inner    

if __name__ == '__main__':

    import time

    @make_visible
    @register('sq')
    @cache
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

    @register('ha')
    def halve(x):
        return x // 2

    @cache
    @make_visible
    def big_func(x):
        'Simulate slow labor intensive function'
        print 'Doing hard work'
        time.sleep(1)
        return x + 1


