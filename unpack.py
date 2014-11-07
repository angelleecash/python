__author__ = 'chenliang'


import glob
import zlib
import sys
import os
from struct import *

filename = '/Users/chenliang/tmp/zuma3/audio.pack'
output = '/Users/chenliang/tmp/output'

total = 0

# raw interface
def rp(c, n, f):
    fc = c.read(n)
    global total
    total += n
    return unpack(f, fc)

# read long
def rl(c):
    return rp(c, 4, '<I')[0]

def skip(c, n):
    c.read(c,n)

# read string
def rs(c):
    size = rl(c)
    # print "string size", size
    s = []
    for i in range(0, size):
        cs = rp(c, 1, 'c')
        s.extend(cs)

    return ''.join(str(x) for x in s)

def rsize(c):
    # how many longs <--------- long represents basic unit
    size = rl(c)

    v = 0
    for i in range(size):
        b = rl(c)
        print hex(b)
        v <<= 32
        v = v | b

    return v

def rbs(c, n):
    bs = []
    for i in range(n):
        bs.extend(rp(c, 1, 'c'))
    return bs




with open(filename, 'rb') as c:
    file_total_length = os.path.getsize(filename)

    id = ''.join(str(x) for x in rp(c, 4, 'cccc'))
    # print id

    for i in range(4):
        # the following longs have their meanings
        # for example size in bytes
        # print rl(c)
        rl(c)

    # Zlib
    rs(c)

    folder_count = rl(c)
    folder_name = rs(c)
    print "folder name:", folder_name

    file_count = rl(c)
    file_names = []
    # print "file count", file_count
    for i in range(file_count):
        # print rs(c)
        file_name = rs(c)
        file_names.append(file_name)
        # print file_name

    rl(c)

    file_lengths = []

    all_size = 0

    for fl in range(80):
        v1 = rl(c)

        v2 = rl(c)
        file_lengths.append(v2)
        all_size += v2
        print "v1=", v1, "v2=", v2

        rbs(c, 4)
        index = rp(c, 1, 'B')
        rbs(c, 7)

    # exit(0)

    all_data = zip(file_names, file_lengths)

    for item in all_data:
        output_file_name = item[0]
        output_file_length = item[1]
        # print "file:", output_file_name, "size:", output_file_length
        # rbs(c, output_file_length)
        bytes = bytearray(rbs(c, output_file_length))

        with open(output + str("/") + str(output_file_name) + ".ogg", 'wb') as expanded:
            expanded.write(bytes)


    if total == file_total_length:
        print "OK"
    else:
        print "Ooops, something went wrong :("


    # c[4:]


# with open(filename, 'r') as compressed:
#         with open(output, 'w') as expanded:
#             data = zlib.decompress(compressed.read())
#             expanded.write(data)

# for filename in sys.argv:
#     with open(filename, 'r') as compressed:
#         with open(filename + "-decompressed', 'w') as expanded:
#         data = zlib.decompress(compressed.read())
#         expanded.write(data)