# Rabat!

## Description

* At some point in your analysis you may come to a point where it appears you need to brute force approximately 10^32 values... there is an easier way if you examine all of the assembly code. No need to brute force this challenge.
* [Attachement](https://ctflearn.com/challenge/download/1060)

## Solution

Using `DIE` , we found it was ELF file.

        Rabat: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), statically linked, not stripped
    
Bắt đầu phân tích chương trình thôi!!

Đề bài cho ta khá nhiều dữ kiện, đừng bác nào đọc tới đoạn 2 số nhân nhau rồi bruceforce tìm 2 số như tôi lúc đầu. Không ra đâu :< Đọc hết toàn bộ đi.

    input[0:7] * input[8:15] = 0x239024F9F888D600A1669A478F0F1F10
    input[0:7] + input[8:15] = 0xBED4CFAAC5C9C25B
    input[16:23] // input[24:27] = 0x17CC632FA
    input[16:23] % input[24:27] = 0x7DE5C8E

    Sum8Byte(input[0:7]) = 0x2A0
    Sum8Byte(input[8:15]) = 0x316
    Sum8Byte(input[16:23]) = 0x15B
    Sum8Byte(input[24:27]) = 0x293
    input[24:27] = 0x37616261

Đề đã cho ta `input[24:27] = "aba7"` ta có thể tính `input[24:27] = Ha55an_R` 
```
def NumberToString(number):
        hex_str = hex(number)[2:]
        ascii_str = ''.join(chr(int(hex_str[i:i+2], 16)) for i in range(0, len(hex_str), 2))
        return ascii_str[::-1]

NumberToString(0x17CC632FA* 0x37616261 + 0x7DE5C8E)
```
Thế còn 16 kí tự đầu thì sao, ta dùng định lý Viette để tìm ra 2 số đó.
```
def find_two_numbers(sum_value, product_value):
    a = 1
    b = -sum_value
    c = product_value
    delta = b**2 - 4 * a * c

    if delta < 0:
        return None

    alpha = (-b + delta**0.5) / (2 * a)
    beta = (-b - delta**0.5) / (2 * a)

    if alpha > 0 and beta > 0:
        return int(alpha), int(beta)
    return None

sum_value = 13750843894638690907
product_value = 47271420571576975187315614910155530000
result = find_two_numbers(sum_value, product_value)

if result:
    x, y = result
    print(f"Hai số cần tìm là {x} và {y}")
    print(f"Tong số cần tìm là {x+y} ")     #   13750843894638690304
    print(f"Tich số cần tìm là {x*y} ")     #   47271420571576971041448812089382535168
else:
    print("Không tìm thấy hai số thỏa mãn yêu cầu.")

# Kết quả: 6877948229877789696 và 6872895664760900608 (sai)
```
Tuy nhiên vì cả 2 số đó đều lớn hơn 2^32, do đó chương trình chỉ nhận 7 byte đầu của số đó. Điều chúng ta cần làm là tìm số đó. Hai tổng có cách biệt 604 đơn vị. Hehehe có cách rồi. 
```
def Sum8Byte(number):
    return sum(bytearray(number.to_bytes(8, byteorder='big')))
def NumberToString(number):
        hex_str = hex(number)[2:]
        ascii_str = ''.join(chr(int(hex_str[i:i+2], 16)) for i in range(0, len(hex_str), 2))
        return ascii_str
x = 6877948229877789696 
y = 6872895664760900608
for i in range(603):
    if (x+i)*(y+603-i)==47271420571576975187315614910155530000:
        print(NumberToString(x+i)[::-1]+NumberToString(y+603-i)[::-1])
        print(hex(Sum8Byte(x+i)),hex(Sum8Byte(y+603-i)))
# Kết quả:  6877948229877790000    0udayas_    0x316
            6872895664760900907    +Med1na_    0x2a0
```
Cảm ơn ``1GN1tE`` đã chia sẻ cách giải bằng z3:
```
from z3 import * 
from pwn import *

x = BitVec('x', 64)
y = BitVec('y', 64)

s = Solver()
s.add(x + y == 0xbed4cfaac5c9c25b)
s.add(x*y == 0x239024f9f888d600a1669a478f0f1f10)

sat = s.check()
model = s.model()

print(p64(int(str(model[x]))).decode())
print(p64(int(str(model[y]))).decode())
```

* Flag:

```
CTFlearn{+Med1na_0udayas_Ha55an_Raba7}
```