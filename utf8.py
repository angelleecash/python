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

def value_to_utf8(v):
    bs = bin(v)[2:].zfill(16)
    b1 = str('1110') + bs[0:4]
    b2 = str('10') + bs[4:10]
    b3 = str('10') + bs[10:]

    ba = bytearray()
    ba.append(int(b1, 2))
    ba.append(int(b2, 2))
    ba.append(int(b3, 2))
    return ba.decode("utf-8")

# for v in range(0x3000, 0x4000):
#     print value_to_utf8(v)

    # br = b1 + b2 + b3
    # bv = int(br, 2)
    # bh = hex(bv)
    # print bh, type(bh), bh.decode("utf-8")

# print value_to_utf8(0x68A0)
print unichr(0x68a0)
c = '梠'
print hex(ord(u'梠'))





