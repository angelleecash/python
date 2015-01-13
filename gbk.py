
# -*- coding: utf-8 -*-

__author__ = 'chenliang'
import unicodedata

import sys
# 二、码位分配及顺序　　
# GBK 亦采用双字节表示，总体编码范围为 8140-FEFE，
# 首字节在 81-FE 之间，尾字节在 40-FE 之间，剔除 xx7F 一条线。
# 总计 23940 个码位，共收入 21886 个汉字和图形符号，其中汉字（包括部首和构件）21003 个，图形符号 883 个。
# D7FA-D7FE 5个空位
# B0A1-F7FE

unicode_to_reading = {}
read_file = open("./read")
for line in read_file:
    segments = line.strip().split("\t")
    unicode_to_reading[segments[0]] = segments[2]

read_file = open("./strokes")
unicode_to_radical_count = {}
unicode_to_radical = {}
#
# print sys.getdefaultencoding()
for line in read_file:
    decoded = line.decode("utf-8")
    segments = decoded.split("\t")

    key = "U+"+hex(ord(segments[1])).upper()[2:]
    unicode_to_radical_count[key] = segments[2]
    unicode_to_radical[key] = segments[11].strip()

for b1 in range(0xB0, 0xF8):
    for b2 in range(0xA1, 0xFF):
        if b2 == 0X7F:
            continue

        if b1 == 0xd7 and (0xfa <= b2 <= 0xfe):
            continue

        bs = bytearray()
        bs.append(b1)
        bs.append(b2)

        vs = bs.decode("GBK")
        key = "U+" + str(hex(ord(vs)))[2:].upper()
        print key, vs, unicode_to_reading[key], unicode_to_radical_count[key], unicode_to_radical[key]
        print "fail to parse ", b1, " ", b2

print "total ", len(unicode_to_reading)