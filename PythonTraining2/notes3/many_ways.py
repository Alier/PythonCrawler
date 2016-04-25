# closures come from a def-in-a-def ######################################################
# Advantage:  Easiest to write

def makepow(base):
    def somepow(exp):
        return pow(base, exp)
    return somepow

twopow, threepow, fourpow, fivepow, sixpow, sevenpow, eightpow = map(makepow, range(2, 9))


# classier way ###########################################################################
# Advantage: It is easy to add other methods to the class than just __call__
# Disadvantage:  Slower than stringy way and closures

class MakePow:

    def __init__(self, base):
        self.base = base

    def __call__(self, exp):
        return pow(self.base, exp)

    def __repr__(self):
        return 'MakePow(base=%r)' % self.base

twopow, threepow, fourpow, fivepow, sixpow, sevenpow, eightpow = map(MakePow, range(2, 9))
        
# stringier way ###########################################################################
# Advantage:  You can build entire modules, execute arbitrary code, output in other languages
# Disadvantage:  Programmers used to all know how to do this and it was normal, now people run scared
# Throwing the baby out with the bath water:
#       Baby:  Exec is awesome and gives you fantastic capabilities
#       Bath water:   Execing arbritrary untrusted, unsantized strings is an EXTREME security risk
#       Throwing-out both:   Eval is evil, exec is evil
#       Correct answer:  Never exec untrusted strings.
#       Summary:  Exec is no more evil than "import", "pickle" "sqlite.execute" "xml"

template = '''\
def somepow(exp):
    return pow({base}, exp)
'''

def string_make_pow(base):
    base = int(base)
    namespace = {}
    exec template.format(base=base) in namespace
    return namespace['somepow']

twopow, threepow, fourpow, fivepow, sixpow, sevenpow, eightpow = map(string_make_pow, range(2, 9))
