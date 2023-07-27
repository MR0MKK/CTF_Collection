# lookup-rev!

## Description

* This program is too slow, what do I do?
* [Attachement](https://imaginaryctf.org/r/E0FA-wpre.py)

## Solution

Chương trình tạo một danh sách các số, kiểm tra có phải số nguyên tố không và XOR với `data` để in ra flag. Tuy nhiên số phép toán thực hiện lớn nên máy tính không thể xử lý hết.

Ta có thể sử dụng hàm `isPrime` để thay thế. Ta in dãy số nguyên tố ra và tìm được đó là dãy `Woodall`. Lên Google tìm 33 kí tự của nó và dùng thôi.
```
from Crypto.Util.number import isPrime
from itertools import count
i = 2
def sequence(index):
    element = (index << index) - 1
    return element
while True:
    if isPrime(sequence(i)):
        print(i)
    i += 1   
```
Lên Google tìm 33 kí tự của nó và dùng thôi.
```
key = [0x6b, 0x60, 0x72, 0x78, 0x30, 0x3d, 0x3f, 0x27, 0x5a, 0x4b, 0x24, 0x61, 0x7b, 0x3, 0x26, 0x68, 0x56,
       0x73, 0x23, 0x49, 0x25, 0x35, 0x34, 0x77, 0x77, 0x22, 0x18, 0x34, 0x77, 0x5a, 0x6b, 0x60, 0x4d]

woodall = [	2, 3, 6, 30, 75, 81, 115, 123, 249, 362, 384, 462, 512, 751, 822, 5312, 7755, 9531, 12379, 15822, 18885, 22971, 23005, 98726, 143018, 151023, 667071, 1195203, 1268979, 1467763, 2013992, 2367906, 3752948, 17016602]

flag = ""

for i in range(len(key)):
    flag+=chr(key[i]^(woodall[i]%100))
print(flag)
```
* Flag:
```
ictf{l00kup_w00dall_pr1me5_78e7f}
```