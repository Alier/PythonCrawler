'Goal:  Build a bitarray class modeled after the bytearray API'

class BitArray:
    'Make a space-efficient array of bits modeled after bytearrays'

    def __init__(self, numbits):
        self.numbits = numbits
        numbytes = -(-numbits // 8)              # ceiling division
        self.data = bytearray(numbytes)

    def __setitem__(self, index, value):
        if index >= self.numbits:
            raise IndexError('BitArray index out of range')
        if value not in {0, 1}:
            raise ValueError('bit must be in the range(0, 2)')
        bytenum, bitnum = divmod(index, 8)
        mask = 1 << bitnum
        if value:
            self.data[bytenum] |= mask
        else:
            self.data[bytenum] &= ~mask

    def __getitem__(self, index):
        if index >= self.numbits:
            raise IndexError('BitArray index out of range')
        bytenum, bitnum = divmod(index, 8)
        return (self.data[bytenum] >> bitnum) & 1

    def __len__(self):
        return self.numbits

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, ''.join(map(str, self)))


if __name__ == '__main__':

    b = BitArray(20)
    b[11] = 1
    b[14] = 1
    b[7] = 1
    b[11] = 0
    print b[11], b[14], b[7], b[19]
    print len(b)
    print list(b)
    print b

