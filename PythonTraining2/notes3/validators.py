'Collections of reusable data validation utilities'

class OneOf(object):

    counter = 0

    def __init__(self, *options):
        self.options = set(options)
        self.private_name = '_one_of_%d' % OneOf.counter
        OneOf.counter += 1

    def __get__(self, obj, objtype=None):
        return getattr(obj, self.private_name)

    def __set__(self, obj, value):
        if value not in self.options:
            raise ValueError('%r must be one of: %r' % (value, self.options))
        setattr(obj, self.private_name, value)
        

    
