# coding=utf-8
import struct
__author__ = 'chenliang'

# b = bytearray([0xe4, 0x80,  0x80])
# c = b.decode(encoding="utf-8")
# print c

# k = bin(0x4000)[2:].zfill(16)
# print k
# print k[0:4]
# print k[0:4] + str('xxyy')
# print k[4:10]
# print k[10:]

for v in range(0x3000, 0x4000):
    bs = bin(v)[2:].zfill(16)
    b1 = str('1110') + bs[0:4]
    b2 = str('10') + bs[4:10]
    b3 = str('10') + bs[10:]

    ba = bytearray()
    ba.append(int(b1, 2))
    ba.append(int(b2, 2))
    ba.append(int(b3, 2))
    print ba.decode("utf-8")

    # br = b1 + b2 + b3
    # bv = int(br, 2)
    # bh = hex(bv)
    # print bh, type(bh), bh.decode("utf-8")






