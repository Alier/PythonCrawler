# Regular way ################################

class Soldier(object):
    'the very model of a modern major general'

    def __init__(self, rank):
        self.rank = rank

    def run(self):
        print 'The %s is running!'% self.rank

    def shoot(self):
        print 'Duck, the %s is shooting!' % self.rank

s = Soldier('Captain')
s.run()
s.shoot()

## Features of a class ########################
print Soldier.__name__, '<== a string with the name given when the class was made'
print Soldier.__bases__, '<== a tuple with the parent classes'
print Soldier.__dict__, '<== data shared by all of its instance plus some metadata'

## Methods of a class ########################
# Soldier = metaclass(name, bases, mapping) ... The metaclass is called 'type'

s = Soldier('Captain') # __call__ makes an instance
print s.rank           # __getattribute__ lookup: instdict -> classdict -> AttributeError, also : implements descriptor
print Soldier          # __repr__ controls the appearance of the class


# New way to make a Soldier class ################################

def __init__(self, rank):
    self.rank = rank

def run(self):
    print 'The %s is running!'% self.rank

def shoot(self):
    print 'Duck, the %s is shooting!' % self.rank

NewSoldier = type('NewSoldier', (object,),
                  dict(
                      __module__ = '__main__',
                      __doc__='The very model of a modern major general',
                      __init__ = __init__,
                      run = run,
                      shoot = shoot,
                    ))

s = NewSoldier('Colonel')
s.run()
s.shoot()
print s

#### Metaclasses are all about customizing how classes work ##############

class CuteReprMeta(type):
    def __repr__(cls):
        return '[[Class %s]]' % cls.__name__


class Soldier3(object):
    'the very model of a modern major general'
    __metaclass__ = CuteReprMeta
    
    def __init__(self, rank):
        self.rank = rank

    def run(self):
        print 'The %s is running!'% self.rank

    def shoot(self):
        print 'Duck, the %s is shooting!' % self.rank

s = Soldier3('General')
s.run()
s.shoot()
print s

NewSoldier2 = CuteReprMeta('NewSoldier', (object,),
                  dict(
                      __module__ = '__main__',
                      __doc__='The very model of a modern major general',
                      __init__ = __init__,
                      run = run,
                      shoot = shoot,
                    ))

s = NewSoldier2('Colonel')
s.run()
s.shoot()
print s

## Instance tracking metaclass #####################
instances = dict()              # args -> instance

class InstanceDedupingMeta(type):
    def __call__(cls, *args):
        if args in instances:
            return instances[args]
        
        inst = type.__call__(cls, *args)
        instances[args] = inst
        return inst

class Soldier4(object):
    'the very model of a modern major general'
    __metaclass__ = InstanceDedupingMeta
    
    def __init__(self, rank):
        self.rank = rank

    def run(self):
        print 'The %s is running!'% self.rank

    def shoot(self):
        print 'Duck, the %s is shooting!' % self.rank

army = map(Soldier4,'private private private corporal lieutenant captain'.split())


## Dynamic and Static attribute metaclass #####################
import time
current_owner ='Raymond'

class CustomAttributeMeta(type):
    def __getattribute__(cls, attr):
        if attr == 'now':
            return time.ctime()
        if attr == 'owner':
            return current_owner
        return type.__getattribute__(cls, attr)

class Soldier5(object):
    'the very model of a modern major general'
    __metaclass__ = CustomAttributeMeta
    
    def __init__(self, rank):
        self.rank = rank

    def run(self):
        print 'The %s is running!'% self.rank

    def shoot(self):
        print 'Duck, the %s is shooting!' % self.rank

s = Soldier5('private')
