# faster -> slower
# locals < nested < globals < attribute

# closures come from a def-in-a-def ####################################

def makepow(base):       #space efficient, all generated functions point to the same reference.
    def somepow(exp):
        return pow(base, exp)
    return somepow

twopow, threepow, fourpow, fivepow, sixpow, sevenpow, eightpow = map(makepow, range(2, 9))


# Classier way ###########################################################
# Pros: It is easy to add other methods to the class than just __call__
# Cons: Slower than stringy way and closures way
class MakePow:
    def __init__(self,base):
        self.base = base

    def __call__(self,exp):
        return pow(self.base, exp)  # attribute lookup is slower than globals lookup


twopow, threepow, fourpow, fivepow, sixpow, sevenpow, eightpow = map(MakePow, range(2,9))

# stringy way ############################################################
# Pros : You can build entire modules, execute arbitrary code, output in other languages
# Cons : Programmers used to all know how to do this and it was normal, now people run scared

func_template = '''\
def somepow(exp):
    return pow({base},exp)
'''

def string_make_pow(base):
    namespace = {}
    exec func_template.format(base=base) in namespace
    return namespace['somepow']

twopow, threepow, fourpow, fivepow, sixpow, sevenpow, eightpow = map(string_make_pow, range(2,9))
