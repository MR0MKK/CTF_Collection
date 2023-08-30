# Danh sách các số hex
hex_list = [0x6d, 0x69, 0x6e, 0x68, 0x6b, 0x69, 0x6e, 0x67]

# Chuyển danh sách các số hex thành một số duy nhất
result_number = 0
for num in hex_list:
    result_number = (result_number << 8) + num

# In kết quả số hex
print(hex(result_number))
