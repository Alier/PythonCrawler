# python -m timeit -s 'x=10' -s 'y=20' 't=x; x=y; y=t'

import time
import itertools

template = '''
def inner(timer, looper):
    {setup}
    start = timer()
    for i in looper:
        {stmt}
    end = timer()
    return end - start
'''

def repeat(stmt, setup='', repetitions=3, times = 10000000):
    code = template.format(setup=setup, stmt=stmt)
    exec code

    timings = []
    for i in range(repetitions):
        timing = inner(time.time, itertools.repeat(None, times))
        timings.append(timing)
    return min(timings) / times


if __name__ == '__main__':

    print repeat(setup='x=10; y=20', stmt='x, y = y, x')






