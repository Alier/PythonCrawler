'Goal:  Develop Jedi skills with lists'

# Basics
# ANYTHING can go in a list

import math

class Dog:
    pass

s = [10]
s.append('hello')
s.append(Dog)
s.append(math.sqrt)
s.append(IndexError)
s.append([20, 30, 40])
s.append(s)

try:
    print s[100]
except s[4]:
    print 'Sorry, the list is not that big'

print s[6][6][6][6][6][6][1]

print map(type, s)

## Singly linked list ###################################
# Pair:  [value, pair-or-None]
# In Lisp, the pair is called a CONS cell
#        , the first field is called CAR
#        , the second field is called CDR
#        , the None is called NIL

VALUE, LINK = 0, 1

s = [10, None]
t = [20, s]
u = [30, t]

def head(p):
    return p[VALUE]

def tail(p):
    return p[LINK]

print head(s)
print head(tail(t))
print head(tail(tail(u)))
print head(tail(u))
print head(u)

def display_linked_list(p):
    while p is not None:
        print head(p)
        p = tail(p)

display_linked_list(u)

print '=' * 30

## Doubly linked list ###################################
# Triple: [value, triple-or-None, triple-or-None]

VALUE, PREV, NEXT = 0, 1, 2

a = ['Raymond', None, None]
b = ['Rachel', a, None];      a[NEXT] = b
c = ['Matthew', b, None];     b[NEXT] = c

print 'Walk forward'
print a[VALUE]
print a[NEXT][VALUE]
print a[NEXT][NEXT][VALUE]

print 'Walk backward'
print c[VALUE]
print c[PREV][VALUE]
print c[PREV][PREV][VALUE]

## Binary Tree ##########################################
# Node:  [value, link-or-None, link-or-None]

NAME, MOM, POP = 0, 1, 2

def person(name, mom=None, pop=None):
    return [name, mom, pop]

sharon, dennis, ramon, gayle = map(person, ['Sharon', 'Dennis', 'Ramon', 'Gayle'])
rachel = person('Rachel', sharon, dennis)
raymond = person('Raymond', gayle, ramon)
matthew = person('Matthew', rachel, raymond)

print 'Grandfathers:'
print '|-> Maternal:', matthew[MOM][POP][NAME]
print '|-> Paternal:', matthew[POP][POP][NAME]

print 'Tree traversal'
print 'There are three classic ways to flatten a tree:  preorder, inorder, postorder'

def preorder(p):
    if p is None:
        return []
    return [p[NAME]] + preorder(p[MOM]) + preorder(p[POP])

def inorder(p):
    if p is None:
        return []
    return inorder(p[MOM]) + [p[NAME]] + inorder(p[POP])

def postorder(p):
    if p is None:
        return []
    return postorder(p[MOM]) + postorder(p[POP]) + [p[NAME]]

print 'Preorder: ', preorder(matthew)
print 'Inorder:  ', inorder(matthew)
print 'Postorder: ', postorder(matthew)
