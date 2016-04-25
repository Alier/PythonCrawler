BLOCKSIZE = 14
NEXT = -2
PREV = -1

class Deque:

    def __init__(self, iterable):
        self.size = 0
        first_block = [None] * (BLOCKSIZE + 2)
        self.leftblock = first_block
        self.leftindex = BLOCKSIZE // 2
        self.rightblock = first_block
        self.rightindex = BLOCKSIZE // 2 - 1
        for element in iterable:
            self.append(element)

    def append(self, element):
        block = self.rightblock
        self.rightindex += 1
        if self.rightindex == BLOCKSIZE:
            new_block = [None] * (BLOCKSIZE + 2)
            block[NEXT] = new_block
            new_block[PREV] = block
            self.rightblock = new_block
            self.rightindex = 0
            block = new_block
        block[self.rightindex] = element

        
        
        
        
        
