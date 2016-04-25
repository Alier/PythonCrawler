'Goal:  Develop a deep understanding of how imports work and how to customize them'

import sys
import os
import urllib

modules = {}

class Module(object):

    def __init__(self, namespace):
        object.__setattr__(self, 'namespace', namespace)

    def __getattr__(self, attrname):
        try:
            return self.namespace[attrname]
        except KeyError:
            raise AttributeError(attrname)

    def __setattr__(self, attrname, value):
        self.namespace[attrname] = value

    def __delattr__(self, attrname):
        try:
            del self.namespace[attrname]
        except KeyError:
            raise AttributeError(attrname)

    def __dir__(self):
        return sorted(self.namespace.keys())

    def __repr__(self):
        return '<Module %r from %r>' % (self.__name__, self.__file__)

def myimport(modname):
    if modname in modules:
        globals()[modname] = modules[modname]
        return

    filename = modname + '.py'
    if filename.startswith('http://'):
        u = urllib.urlopen(filename)
        code = u.read()
        modname = os.path.split(modname)[1]
    else:
        for dirname in sys.path:
            fullname = os.path.join(dirname, filename)
            try:
                with open(fullname) as f:
                    code = f.read()
                break
            except IOError:
                pass
        else:
            raise ImportError('No module named %s' % modname)

    namespace = {}
    namespace['__name__'] = modname
    namespace['__file__'] = filename
    namespace['__package__'] = None
    exec code in namespace
    module = Module(namespace)
    modules[modname] = module
    globals()[modname] = module

def myreload(module):
    modname = module.__name__
    del modules[modname]
    myimport(modname)
    return modules[modname]

if __name__ == '__main__':

    myimport('sample')
    print sample.n
    print sample.cube(11)

    myimport('random')
    print random.randrange(500)

    myimport('http://users.rcn.com/python/download/puzzle')

