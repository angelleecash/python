__author__ = 'chenliang'
#encoding=utf8
import unicodedata

import sys
# 二、码位分配及顺序　　
# GBK 亦采用双字节表示，总体编码范围为 8140-FEFE，
# 首字节在 81-FE 之间，尾字节在 40-FE 之间，剔除 xx7F 一条线。
# 总计 23940 个码位，共收入 21886 个汉字和图形符号，其中汉字（包括部首和构件）21003 个，图形符号 883 个。
# D7FA-D7FE 5个空位
# B0A1-F7FE

unicode_to_reading = {}
read_file = open("/Users/chenliang/read")
for line in read_file:
    segments = line.strip().split("\t")
    unicode_to_reading[segments[0]] = segments[2]

# read_file = open("/Users/chenliang/git_projects/pythons/strokes")
read_file = open("./strokes")
unicode_to_radical_count = {}
# kkk = read_file.read().decode(encoding="utf8")
# print kkk
#
# print sys.getdefaultencoding()
for line in read_file:
    decoded = line.decode("utf-8")
    segments = decoded.split("\t")
    # print segments[0], segments[1], type(segments[0]), type(segments[1]), segments[1]

    # for v in segments:
    #     print type(v), v, len(v)
    # exit()
    # , ord(segments[0])
    # print line, len(segments)
    # print line
    # for i in range(0, len(segments)):
    #     print i, segments[i]
    #
    # print "------------------------------------------------\n"
    print segments[1], repr(segments[1]), ord(segments[1])
    # key = "U+"+hex(ord(segments[1])).upper()[2:]
    # unicode_to_radical_count[key] = segments[2]
    # 1,2,4,5,6,7,8,9,11
    # print segments[0],segments[1],segments[3],segments[4],segments[5],segments[6],segments[7],segments[8],segments[10]
    # print type(segments[0]), segments[0], decoded, "---------", line
    # ch = segments[0].decode("utf-8")
    # try:
    #     key = "U+"+hex(ord(ch)).upper()[2:]
    #     print "key=", key
    #     unicode_to_radical_count[key] = segments[1]
    # except Exception as e:
    #     print "fail for ", ch
    #     pass
    # "U+"+hex(ord(segments[0])).upper()[2:]

    # print segments[0][0], type(segments[0][0]), len(segments[0][0])

exit()

for b1 in range(0xB0, 0xF8):
    for b2 in range(0xA1, 0xFF):
        if b2 == 0X7F:
            continue

        if b1 == 0xd7 and (0xfa <= b2 <= 0xfe):
            continue

        bs = bytearray()
        bs.append(b1)
        bs.append(b2)

        try:
            vs = bs.decode("GBK")
            key = "U+"+str(hex(ord(vs)))[2:].upper()
            print key, vs, unicode_to_reading[key], unicode_to_radical_count[key]
        except:
            print "fail to parse ", b1, " ", b2
            pass

# ba = bytearray()
# ba.append(215)
# ba.append(250)
#
# ba.decode("GBK")

# bs = bytearray();
# bs.append(0x4E)
# bs.append(0x24)
#
# print bs.decode("GB2312")