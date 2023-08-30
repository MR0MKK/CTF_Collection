v4 = [283, 171, 159, 78, 112, 299, 76, 166, 257, 145, 124, 72, 170, 300, 149, 132, 86, 231, 219, 96, 239, 224, 190, 197]
key = [0xEA, 0x0C, 0xA5, 0x13, 0xE6, 0x7E, 0xFE, 0x09, 0xAE, 0x2E, 0x94, 0x07, 0xB8, 0xBC, 0x10, 0x132, 0xB7, 0x16B, 0x174, 0xD9, 0x96, 0xCC, 0x94, 0x151]
temp = {}
flag = ""
def sleep(value):
    if (value & 1 ) != 0:
        return value * 66 + 5
    else:
        return value * (value % 10 +132)
for i in range(len(v4)):
    temp[v4[i]]=sleep(v4[i])
# temp.sort()
print(temp)

# for i in range(len(temp)):
#     for j in range(len(v4)):
#         if temp[v4[i]] == sleep(v4[j]):
#             print(v4[j],hex(key[i]))
#             flag += chr(v4[j] ^ key[i])
# print(flag)


# v4 = [283, 171, 159, 78, 112, 299, 76, 166, 257, 145, 124, 72, 170, 300, 149, 132, 86, 231, 219, 96, 239, 224, 190, 197]
# flag=""
# key = [0xEA, 0x0C, 0xA5, 0x13, 0xE6, 0x7E, 0xFE, 0x09, 0xAE, 0x2E, 0x94, 0x07, 0xB8, 0xBC, 0x10, 0x132, 0xB7, 0x16B, 0x174, 0xD9, 0x96, 0xCC, 0x94, 0x151]
# for i in key:
#     for k in v4:
#         xor_result = i ^ k  
#         if 0x40 <= xor_result <= 0x7E:
#             flag+=chr(xor_result)
# print(flag)
   
# print(145^0xea)