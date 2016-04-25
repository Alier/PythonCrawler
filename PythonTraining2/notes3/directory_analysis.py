'Goal:  First the most common file extensions (by size) in a directory'

import os
from collections import namedtuple, Counter

FileInfo = namedtuple('FileInfo', ['filename', 'ext', 'size'])

def scandir(dirname):
    'Return a list of FileInfo for all the files in a directory'
    dirinfo = []
    for filename in os.listdir(dirname):
        base, ext = os.path.splitext(filename)
        fullname = os.path.join(dirname, filename)
        size = os.stat(fullname).st_size
        fileinfo = FileInfo(filename, ext, size)
        dirinfo.append(fileinfo)
    return dirinfo

def dominant_extensions(dirname, limit=5):
    'Show which file extensions take the most space'
    extsize = Counter()
    for fileinfo in scandir(dirname):
        extsize[fileinfo.ext] += fileinfo.size
    return extsize.most_common(limit)

if __name__ == '__main__':
    from pprint import pprint

    pprint(dominant_extensions('notes3'))

