__author__ = 'chenliang'
#encoding=utf8

# 二、码位分配及顺序　　
# GBK 亦采用双字节表示，总体编码范围为 8140-FEFE，
# 首字节在 81-FE 之间，尾字节在 40-FE 之间，剔除 xx7F 一条线。
# 总计 23940 个码位，共收入 21886 个汉字和图形符号，其中汉字（包括部首和构件）21003 个，图形符号 883 个。

# B0A1-F7FE

# for b1 in range(0xB0, 0xF8):
#     for b2 in range(0xA1, 0xFF):
#         if b2 == 0X7F:
#             continue;
#
#         bs = bytearray();
#         bs.append(b1)
#         bs.append(b2)
#
#         try:
#             vs = bs.decode("GBK")
#             print vs
#         except:
#             print "fail to parse ", b1, " ", b2
#             pass

bs = bytearray();
bs.append(0x4E)
bs.append(0x24)

print bs.decode("GB2312")