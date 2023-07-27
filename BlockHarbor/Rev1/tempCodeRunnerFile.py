
import ctypes
def uint32(num):
    return ctypes.c_uint32(num).value 
start = [0]*4
char1=  0x61 
char2=  0x62
char3=  0x63
char4=  0x64


start[0] |= char1 << 24
start[0] |= char2 << 16
start[0] |= char3 << 8
start[0] |= char4

temp = start[0]
temp *= 0xcafebeef
temp += 78629421
temp *= 0xfacefeed
temp ^= 1554612952

aaaa = uint32(temp)
print(aaaa)

