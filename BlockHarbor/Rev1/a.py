import ctypes

def uint32(num):
    return ctypes.c_uint32(num).value  

def check_pass(start):
    # data = [0x1e48add6, 0xaaa7550c, 0x18df53bf, 0xe6af1116]
    data = [508079574, 2863093004, 417289151, 3870232854]
    # for i in range(4):
    temp = start[0]
    temp *= 0xcafebeef
    temp += 78629421
    temp *= 0xfacefeed
    temp ^= 1554612952
    a = uint32(temp)
    if a == 64842860:   #347574740
        print(start)
    # print(a)
    if a in data:
        print(start,data.index(a))
    # else:
    #     break


def main():
    

    start = [0]*4
    # for i in range(4):
    for char1 in range(0x30, 0x7E):
        for char2 in range(0x30, 0x7E):
            for char3 in range(0x30, 0x7E):
                for char4 in range(0x30, 0x7E):
                    
                    start[0] |= char1 << 24
                    start[0] |= char2 << 16
                    start[0] |= char3 << 8
                    start[0] |= char4
                    
                    check_pass(start)
                    start[0] = 0

if __name__ == "__main__":
    main()

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

