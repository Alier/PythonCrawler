''' Goal:  Show how event loop work.
           Understand callback style programming
           Learn patterns of callback programming in event loops
           Practice heaps, namedtuples, partial, time module
           Develop an insight into Twisted, Tornado, Diesel, sched, and other popular event loops.
'''

from collections import deque, namedtuple
from functools import partial
from heapq import heappush, heappop
from time import time, sleep
from pprint import pprint

Event = namedtuple('Event', ['event_time', 'task'])

events = []

def add_event(event_time, task):
    heappush(events, Event(event_time, task))

def call_later(delay, task):
    add_event(time() + delay, task)

def call_periodic(delay, interval, task):
    'Starting at time()+delay, run the task repeatedly as fixed intervals'
    def inner():
        task()
        call_later(interval, inner)
    call_later(delay, inner)

def event_loop():
    while events:
        while events[0].event_time > time():
            sleep(0.1)
        event = heappop(events)
        event.task()

#################################################################################

def show_msg(text):
    print text

def show_two():
    print 'Two!'

def show_ten():
    print 'Ten'

def show_five_three_times():
    call_later(5, partial(show_msg, 'Five'))
    call_later(15, partial(show_msg, 'Five'))
    call_later(28, partial(show_msg, 'Five'))

call_periodic(13, 2, partial(show_msg, 'Heartbeat!'))
call_later(10, show_two)
call_later(5, show_ten)
call_later(20, show_two)
call_later(1, partial(show_msg, 'Howdy'))
call_later(35, partial(show_msg, "C'ya!"))
call_later(8, show_five_three_times)

event_loop()
