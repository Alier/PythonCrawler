''' Goal:  Learn to generate code automatically from specs
           as a way to save labor and improve quality.
'''

def parse(data):
    'Parse a variable length record format'
    i = 0
    while i < len(data):
        kind = data[i]
        i += 1
        if 0:
            pass
        elif kind == 'p':
            lastname = str(data[i:i+8]).rstrip()
            i += 8
            age = int(data[i:i+4])
            i += 4
            print dict(kind=kind, lastname=lastname, age=age)
        elif kind == 'c':
            firstname = str(data[i:i+10]).rstrip()
            i += 10
            height = float(data[i:i+12])
            i += 12
            print dict(kind=kind, firstname=firstname, height=height)
        else:
            raise ValueError('Unknown kind: ' + kind)

if 0:
    sample_data = 'pSmith     15pJones      9cRaymond           63.7'
    parse(sample_data)


###########################################
####### Your Turn.    Class Exercise ######

# Hint 1:  start with a debugged working code fragment
# Hint 2:  cut-and-paste, then parameterize
# Hint 3:  use multi-line strings with a leading backslash
# Hint 4:  work from inside out
# Hint 5:  arrange your templates in the same order as the original file
# Hint 6:  start with global variables, then move to a function
# Hint 7:  develop using print, then turn into a generator
# Hint 8:  combine the strings and exec

header = '''\
def parse(data):
    'Parse a variable length record format'
    i = 0
    while i < len(data):
        kind = data[i]
        i += 1
        if 0:
            pass
'''

kind_line = '''\
        elif kind == '{kind}':
'''

str_line = '''\
            {fname} = str(data[i:i+{fwidth}]).rstrip()
            i += {fwidth}
'''

other_line = '''\
            {fname} = {ftype.__name__}(data[i:i+{fwidth}])
            i += {fwidth}
'''

pair_template = '{fname}={fname}'

pair_joiner = ', '

dict_line = '''\
            print dict(kind=kind, {pairs})
'''

footer = '''\
        else:
            raise ValueError('Unknown kind: ' + kind)
'''

def generate_parse_function(record_layout):
    yield header
    for kind, fspecs in record_layout.items():
        yield kind_line.format(kind=kind)
        for fname, ftype, fwidth in fspecs:
            if ftype == str:
                yield str_line.format(fname=fname, fwidth=fwidth)
            else:
                yield other_line.format(fname=fname, ftype=ftype, fwidth=fwidth)
        pairs = [pair_template.format(fname=fname) for fname, ftype, fwidth in fspecs]
        yield dict_line.format(pairs=pair_joiner.join(pairs))
    yield footer

def parse_record_type(record_layout, verbose=True):
    g = generate_parse_function(record_layout)
    code = ''.join(g)
    if verbose:
        print code
    namespace = {}
    exec code in globals(), namespace
    return namespace['parse']

###########################################
#######    Client Code               ######

if 1:

    record_layout = {
        'p': [('lastname', str, 8), ('age', int, 4)],
        'c': [('firstname', str, 10), ('height', float, 12)],
        'd': [('coursename', str, 20), ('coursenumber', int, 4)],
        'q': [('military_id', str, 12), ('blood_type', str, 2), ('rank', int, 2)],
        'n': [('station_name', str, 13), ('station_number', int, 5), ('response_time', float, 8)],
        'a': [('hometown', str, 20), ('pop_density', float, 15), ('long', float, 8),
              ('lat', float, 4)],
    }
    parse = parse_record_type(record_layout, verbose=True)
    sample_data = 'pSmith     15pJones      9cRaymond           63.7'
    parse(sample_data)

