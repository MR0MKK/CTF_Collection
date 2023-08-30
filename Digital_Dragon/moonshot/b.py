part1 = False
part2 = False

def FUN_00101160(a1, a2, a3, a4, a5, a6, a7):
    global part1, part2
    
    result = None
    
    if not part1:
        print(chr(a7 | a6 | a3 | a2))
        print(chr(a7 | a6 | a4 | a3))
        print(chr(a7 | a6 | a1))
        print(chr(a7 | a6 | a3 | a2 | a1))
        print(chr(a7 | a6 | a5 | a4 | a2 | a1))
        part1 = True
    
    if part1:
        print(chr(a7 | a6 | a5 | a3 | a2 | a1))
        print(chr(a7 | a6 | a4))
        print(chr(a7 | a6 | a1))
        print(chr(a7 | a6 | a5 | a3))
        print(chr(a7 | a5 | a4 | a3 | a2 | a1))
        print(chr(a7 | a6 | a1))
        print(chr(a7 | a5 | a4 | a3 | a2 | a1))
        print(chr(a7 | a6 | a4 | a3 | a1))
        print(chr(a7 | a6 | a3 | a1))
        print(chr(a7 | a6 | a5 | a2 | a1))
        print(chr(a7 | a6 | a5 | a2 | a1))
        part2 = True
    
    result = part2
    
    if not part2:
        return result
    
    print(chr(a7 | a6 | a5 | a4 | a3 | a1))
    return print(chr(a4 | a2))

v26 = 0x1010101&0xff
v25 = 0x2020202&0xff
v24 = 0x4040404&0xff
v23 = 0x8080808&0xff
v22 = 0x10101010&0xff
v21 = 0x20202020&0xff
v20 = 0x40404040&0xff
v19 = 0x80808080&0xff

FUN_00101160(v26, v25, v24, v23, v22, v21, v20)


v19 = 0x80808080
print(hex(v19&0xff))