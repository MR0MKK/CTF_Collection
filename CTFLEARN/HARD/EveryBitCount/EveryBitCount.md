# Every Bit Count!

## Description

* My colleague is a senior C developer and he had a bad experience in his job assignment. He was developing applications for a real-time embedded operating system named "Buggy OS™". He had to implement workarounds to avoid using the standard C library in some cases. For instance the memcmp shouldn't be used to test command-line argument because of obscure reason resulting in some bits were not checked. Instead he implemented its own function to check each bit of the command-line and it was working fine.
* [Attachement](https://ctflearn.com/challenge/download/921)

## Solution

1. Using `DIE` , we found it was ELF file. 

       every_bit_counts: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, stripped

2. Using  `IDA64` to analys file



![Imgur](https://i.imgur.com/Rfd7MXh.png)

![Imgur](https://i.imgur.com/wSxsMF9.png)

Khiếp quá, phải dùng z3 hoặc angr để nó tính toán hộ mình!!

```
from z3 import *

condition =["(flag[28] & 0x20) == 0" , "(flag[36] & 0x10) != 0" , "(flag[47] & 0x20) != 0" , "(flag[32] & 0x20) != 0" , "(flag[43] & 4) != 0" , "(flag[50] & 0x80) == 0" , "(flag[8] & 1) != 0" , "(flag[46] & 4) != 0" , "(flag[32] & 0x80) == 0" , "(flag[8] & 4) == 0" , "(flag[48] & 0x10) != 0" , "(flag[16] & 0x80) == 0" , "(flag[19] & 8) == 0" , "(flag[8] & 0x40) != 0" , "(flag[43] & 0x10) != 0" , "(flag[15] & 4) != 0" , "(flag[0] & 4) == 0" , "(flag[43] & 8) == 0" , "(flag[25] & 0x40) != 0" , "(flag[4] & 1) != 0" , "(flag[43] & 0x80) == 0" , "(flag[44] & 8) == 0" , "(flag[33] & 0x20) != 0" , "(flag[29] & 0x10) == 0" , "(flag[33] & 1) != 0" , "(flag[28] & 0x40) != 0" , "(flag[23] & 0x40) != 0" , "(flag[24] & 1) != 0" , "(flag[39] & 0x20) != 0" , "(flag[37] & 4) == 0" , "(flag[13] & 0x80) == 0" , "(flag[49] & 0x20) != 0" , "(flag[9] & 4) != 0" , "(flag[7] & 0x20) != 0" , "(flag[48] & 4) == 0" , "(flag[18] & 4) == 0" , "(flag[45] & 4) == 0" , "(flag[30] & 0x10) != 0" , "(flag[7] & 0x10) == 0" , "(flag[49] & 0x40) != 0" , "(flag[2] & 0x80) == 0" , "(flag[12] & 0x40) != 0" , "(flag[37] & 8) == 0" , "(flag[29] & 8) == 0" , "(flag[29] & 0x20) != 0" , "(flag[50] & 2) != 0" , "(flag[45] & 1) == 0" , "(flag[10] & 0x10) != 0" , "(flag[40] & 0x80) == 0" , "(flag[18] & 2) == 0" , "(flag[43] & 1) != 0" , "(flag[26] & 0x80) == 0" , "(flag[51] & 0x80) == 0" , "(flag[20] & 4) != 0" , "(flag[30] & 8) != 0" , "(flag[4] & 0x10) == 0" , "(flag[4] & 0x80) == 0" , "(flag[21] & 0x40) != 0" , "(flag[23] & 0x80) == 0" , "(flag[12] & 0x10) != 0" , "(flag[41] & 1) != 0" , "(flag[13] & 0x20) != 0" , "(flag[36] & 1) == 0" , "(flag[1] & 1) == 0" , "(flag[19] & 0x80) == 0" , "(flag[5] & 0x80) == 0" , "(flag[50] & 0x40) == 0" , "(flag[8] & 0x10) != 0" , "(flag[35] & 8) == 0" , "(flag[9] & 8) == 0" , "(flag[0] & 2) != 0" , "(flag[21] & 0x80) == 0" , "(flag[7] & 1) == 0" , "(flag[41] & 8) != 0" , "(flag[3] & 0x80) == 0" , "(flag[14] & 2) != 0" , "(flag[22] & 2) != 0" , "(flag[23] & 1) != 0" , "(flag[39] & 2) != 0" , "(flag[16] & 0x20) == 0" , "(flag[6] & 8) == 0" , "(flag[26] & 1) == 0" , "(flag[30] & 4) != 0" , "(flag[26] & 2) != 0" , "(flag[30] & 0x80) == 0" , "(flag[22] & 0x80) == 0" , "(flag[35] & 0x10) == 0" , "(flag[48] & 1) != 0" , "(flag[33] & 4) != 0" , "(flag[4] & 4) != 0" , "(flag[36] & 0x80) == 0" , "(flag[31] & 8) != 0" , "(flag[1] & 2) == 0" , "(flag[34] & 4) != 0" , "(flag[16] & 1) != 0" , "(flag[3] & 0x10) == 0" , "(flag[22] & 0x10) != 0" , "(flag[42] & 1) != 0" , "(flag[11] & 1) != 0" , "(flag[1] & 0x10) != 0" , "(flag[2] & 4) != 0" , "(flag[10] & 8) == 0" , "(flag[19] & 1) != 0" , "(flag[36] & 8) == 0" , "(flag[4] & 8) == 0" , "(flag[2] & 1) == 0" , "(flag[27] & 0x10) == 0" , "(flag[9] & 1) != 0" , "(flag[13] & 2) == 0" , "(flag[5] & 0x20) != 0" , "(flag[17] & 0x10) == 0" , "(flag[13] & 0x10) != 0" , "(flag[13] & 0x40) != 0" , "(flag[3] & 4) != 0" , "(flag[7] & 2) != 0" , "(flag[16] & 2) != 0" , "(flag[32] & 8) == 0" , "(flag[35] & 2) == 0" , "(flag[49] & 8) == 0" , "(flag[27] & 4) != 0" , "(flag[47] & 0x80) == 0" , "(flag[13] & 8) != 0" , "(flag[1] & 0x80) == 0" , "(flag[38] & 0x80) == 0" , "(flag[36] & 4) == 0" , "(flag[51] & 0x10) != 0" , "(flag[23] & 0x20) == 0" , "(flag[6] & 2) != 0" , "(flag[35] & 0x80) == 0" , "(flag[20] & 0x20) != 0" , "(flag[9] & 0x20) != 0" , "(flag[45] & 0x20) != 0" , "(flag[12] & 2) != 0" , "(flag[6] & 0x10) != 0" , "(flag[34] & 8) != 0" , "(flag[26] & 0x20) != 0" , "(flag[23] & 2) == 0" , "(flag[14] & 0x10) == 0" , "(flag[12] & 8) != 0" , "(flag[34] & 0x80) == 0" , "(flag[16] & 4) != 0" , "(flag[3] & 2) == 0" , "(flag[49] & 2) != 0" , "(flag[22] & 0x20) == 0" , "(flag[21] & 0x20) != 0" , "(flag[41] & 0x20) == 0" , "(flag[37] & 2) != 0" , "(flag[18] & 0x80) == 0" , "(flag[7] & 4) != 0" , "(flag[47] & 4) != 0" , "(flag[10] & 2) == 0" , "(flag[11] & 0x80) == 0" , "(flag[32] & 4) == 0" , "(flag[38] & 0x40) != 0" , "(flag[0] & 0x10) == 0" , "(flag[2] & 0x40) != 0" , "(flag[28] & 0x80) == 0" , "(flag[43] & 0x40) != 0" , "(flag[47] & 8) != 0" , "(flag[44] & 0x20) != 0" , "(flag[24] & 0x20) != 0" , "(flag[9] & 2) != 0" , "(flag[6] & 4) == 0" , "(flag[49] & 4) == 0" , "(flag[0] & 8) == 0" , "(flag[11] & 0x40) != 0" , "(flag[5] & 1) != 0" , "(flag[20] & 8) != 0" , "(flag[47] & 0x40) != 0" , "(flag[38] & 8) != 0" , "(flag[25] & 4) != 0" , "(flag[33] & 0x80) == 0" , "(flag[5] & 8) == 0" , "(flag[40] & 0x10) == 0" , "(flag[25] & 0x10) != 0" , "(flag[37] & 1) != 0" , "(flag[2] & 8) == 0" , "(flag[42] & 0x40) != 0" , "(flag[9] & 0x10) != 0" , "(flag[46] & 0x80) == 0" , "(flag[41] & 4) != 0" , "(flag[41] & 0x10) != 0" , "(flag[29] & 0x80) == 0" , "(flag[0] & 0x20) == 0" , "(flag[37] & 0x40) == 0" , "(flag[25] & 0x80) == 0" , "(flag[23] & 0x10) == 0" , "(flag[27] & 1) == 0" , "(flag[15] & 0x10) != 0" , "(flag[31] & 0x40) != 0" , "(flag[42] & 0x10) == 0" , "(flag[10] & 0x20) != 0" , "(flag[48] & 0x40) == 0" , "(flag[15] & 0x80) == 0" , "(flag[28] & 8) == 0" , "(flag[39] & 1) != 0" , "(flag[40] & 2) != 0" , "(flag[50] & 4) == 0" , "(flag[39] & 0x10) != 0" , "(flag[42] & 4) != 0" , "(flag[45] & 8) != 0" , "(flag[13] & 4) == 0" , "(flag[51] & 0x20) != 0" , "(flag[21] & 8) == 0" , "(flag[32] & 2) == 0" , "(flag[29] & 4) != 0" , "(flag[30] & 1) != 0" , "(flag[44] & 2) != 0" , "(flag[3] & 8) != 0" , "(flag[10] & 0x80) == 0" , "(flag[51] & 2) == 0" , "(flag[38] & 1) != 0" , "(flag[19] & 0x40) != 0" , "(flag[39] & 0x40) != 0" , "(flag[27] & 0x20) != 0" , "(flag[45] & 0x40) != 0" , "(flag[2] & 2) != 0" , "(flag[27] & 8) != 0" , "(flag[11] & 0x10) != 0" , "(flag[24] & 0x40) != 0" , "(flag[5] & 2) == 0" , "(flag[25] & 2) != 0" , "(flag[26] & 0x40) != 0" , "(flag[24] & 4) == 0" , "(flag[4] & 0x40) != 0" , "(flag[47] & 0x10) == 0" , "(flag[41] & 0x40) != 0" , "(flag[34] & 0x10) != 0" , "(flag[35] & 0x40) != 0" , "(flag[5] & 4) == 0" , "(flag[21] & 2) == 0" , "(flag[45] & 0x10) == 0" , "(flag[36] & 2) != 0" , "(flag[40] & 0x40) != 0" , "(flag[21] & 4) != 0" , "(flag[19] & 4) != 0" , "(flag[12] & 0x80) == 0" , "(flag[42] & 2) == 0" , "(flag[1] & 8) == 0" , "(flag[16] & 0x10) != 0" , "(flag[35] & 4) == 0" , "(flag[13] & 1) != 0" , "(flag[1] & 0x40) != 0" , "(flag[46] & 1) != 0" , "(flag[31] & 0x10) != 0" , "(flag[38] & 4) != 0" , "(flag[47] & 2) != 0" , "(flag[38] & 2) != 0" , "(flag[37] & 0x80) == 0" , "(flag[28] & 2) == 0" , "(flag[10] & 0x40) == 0" , "(flag[46] & 0x10) != 0" , "(flag[39] & 0x80) == 0" , "(flag[46] & 0x20) == 0" , "(flag[31] & 1) != 0" , "(flag[37] & 0x10) != 0" , "(flag[0] & 1) != 0" , "(flag[17] & 0x20) != 0" , "(flag[11] & 0x20) != 0" , "(flag[49] & 0x80) == 0" , "(flag[18] & 8) == 0" , "(flag[22] & 0x40) != 0" , "(flag[28] & 4) == 0" , "(flag[14] & 8) != 0" , "(flag[48] & 8) == 0" , "(flag[6] & 0x40) != 0" , "(flag[12] & 0x20) == 0" , "(flag[48] & 0x20) != 0" , "(flag[31] & 4) == 0" , "(flag[46] & 0x40) != 0" , "(flag[33] & 8) == 0" , "(flag[42] & 0x80) == 0" , "(flag[15] & 1) != 0" , "(flag[24] & 0x80) == 0" , "(flag[12] & 4) != 0" , "(flag[21] & 0x10) == 0" , "(flag[21] & 1) == 0" , "(flag[31] & 0x20) != 0" , "(flag[26] & 4) != 0" , "(flag[51] & 0x40) != 0" , "(flag[42] & 0x20) != 0" , "(flag[12] & 1) != 0" , "(flag[15] & 8) == 0" , "(flag[27] & 0x80) == 0" , "(flag[34] & 2) != 0" , "(flag[6] & 0x20) != 0" , "(flag[23] & 8) != 0" , "(flag[39] & 4) == 0" , "(flag[18] & 1) == 0" , "(flag[32] & 0x10) != 0" , "(flag[28] & 1) == 0" , "(flag[46] & 2) != 0" , "(flag[11] & 2) != 0" , "(flag[28] & 0x10) == 0" , "(flag[29] & 2) != 0" , "(flag[47] & 1) == 0" , "(flag[17] & 4) != 0" , "(flag[14] & 0x20) != 0" , "(flag[43] & 2) == 0" , "(flag[31] & 0x80) == 0" , "(flag[31] & 2) == 0" , "(flag[35] & 0x20) == 0" , "(flag[15] & 0x40) != 0" , "(flag[30] & 0x20) == 0" , "(flag[45] & 0x80) == 0" , "(flag[9] & 0x40) != 0" , "(flag[7] & 8) != 0" , "(flag[0] & 0x80) == 0" , "(flag[38] & 0x20) == 0" , "(flag[37] & 0x20) != 0" , "(flag[22] & 1) != 0" , "(flag[50] & 0x10) != 0" , "(flag[51] & 4) != 0" , "(flag[44] & 0x10) == 0" , "(flag[25] & 0x20) == 0" , "(flag[34] & 0x20) == 0" , "(flag[44] & 0x80) == 0" , "(flag[5] & 0x10) == 0" , "(flag[0] & 0x40) != 0" , "(flag[20] & 0x10) == 0" , "(flag[8] & 8) != 0" , "(flag[17] & 0x80) == 0" , "(flag[35] & 1) != 0" , "(flag[33] & 0x10) != 0" , "(flag[32] & 1) == 0" , "(flag[39] & 8) == 0" , "(flag[4] & 0x20) != 0" , "(flag[22] & 4) != 0" , "(flag[14] & 0x80) == 0" , "(flag[20] & 0x80) == 0" , "(flag[20] & 2) != 0" , "(flag[23] & 4) != 0" , "(flag[43] & 0x20) != 0" , "(flag[34] & 1) != 0" , "(flag[36] & 0x20) != 0" , "(flag[46] & 8) != 0" , "(flag[30] & 2) != 0" , "(flag[8] & 0x20) != 0" , "(flag[17] & 2) != 0" , "(flag[27] & 2) == 0" , "(flag[19] & 2) == 0" , "(flag[7] & 0x80) == 0" , "(flag[3] & 1) == 0" , "(flag[1] & 0x20) == 0" , "(flag[30] & 0x40) != 0" , "(flag[5] & 0x40) != 0" , "(flag[34] & 0x40) != 0" , "(flag[26] & 0x10) == 0" , "(flag[3] & 0x40) != 0" , "(flag[41] & 0x80) == 0" , "(flag[40] & 1) != 0" , "(flag[45] & 2) == 0" , "(flag[1] & 4) != 0" , "(flag[26] & 8) == 0" , "(flag[48] & 0x80) == 0" , "(flag[25] & 8) != 0" , "(flag[17] & 0x40) != 0" , "(flag[29] & 1) != 0" , "(flag[33] & 0x40) != 0" , "(flag[27] & 0x40) != 0" , "(flag[25] & 1) != 0" , "(flag[10] & 1) == 0" , "(flag[4] & 2) == 0" , "(flag[40] & 4) != 0" , "(flag[8] & 2) != 0" , "(flag[15] & 2) == 0" , "(flag[14] & 1) != 0" , "(flag[10] & 4) == 0" , "(flag[42] & 8) != 0" , "(flag[50] & 8) == 0" , "(flag[38] & 0x10) != 0" , "(flag[50] & 1) != 0" , "(flag[2] & 0x10) == 0" , "(flag[51] & 1) != 0" , "(flag[44] & 4) == 0" , "(flag[29] & 0x40) != 0" , "(flag[16] & 0x40) != 0" , "(flag[24] & 0x10) != 0" , "(flag[18] & 0x20) != 0" , "(flag[18] & 0x40) == 0" , "(flag[20] & 0x40) != 0" , "(flag[32] & 0x40) == 0" , "(flag[11] & 4) != 0" , "(flag[3] & 0x20) != 0" , "(flag[2] & 0x20) == 0" , "(flag[7] & 0x40) != 0" , "(flag[41] & 2) != 0" , "(flag[49] & 0x10) == 0" , "(flag[9] & 0x80) == 0" , "(flag[48] & 2) == 0" , "(flag[24] & 2) == 0" , "(flag[36] & 0x40) != 0" , "(flag[17] & 1) == 0" , "(flag[18] & 0x10) != 0" ,
 "(flag[19] & 0x10) != 0" , "(flag[50] & 0x20) != 0" , "(flag[40] & 0x20) != 0" , "(flag[44] & 0x40) != 0" , "(flag[51] & 8) != 0" , "(flag[14] & 4) != 0" , "(flag[6] & 0x80) == 0" , "(flag[17] & 8) == 0" , "(flag[22] & 8) != 0" , "(flag[33] & 2) == 0" , "(flag[20] & 1) == 0" , "(flag[6] & 1) == 0" , "(flag[19] & 0x20) != 0" , "(flag[8] & 0x80) == 0" , "(flag[16] & 8) != 0" , "(flag[15] & 0x20) != 0" , "(flag[11] & 8) == 0" , "(flag[24] & 8) != 0" , "(flag[14] & 0x40) != 0" , "(flag[40] & 8) != 0" , "(flag[49] & 1) != 0" , "(flag[44] & 1) != 0" ]

final = []

flag = [BitVec(f'arr[{i}]',64) for i in range(52)]

s = Solver()

for i in condition:
    s.add(eval(i))

print(s.check())
print(s.model())
```
```
arr = [0]*52

arr[24] = 121
arr[1] = 84
arr[29] = 103
arr[37] = 51
arr[0] = 67
arr[3] = 108
arr[9] = 119
arr[19] = 117
arr[34] = 95
arr[49] = 99
arr[44] = 99
arr[30] = 95
arr[2] = 70
arr[5] = 97
arr[31] = 121
arr[38] = 95
arr[10] = 48
arr[8] = 123
arr[47] = 110
arr[11] = 119
arr[22] = 95
arr[45] = 104
arr[20] = 110
arr[6] = 114
arr[36] = 114
arr[12] = 95
arr[51] = 125
arr[21] = 100
arr[42] = 109
arr[18] = 48
arr[14] = 111
arr[32] = 48
arr[7] = 110
arr[13] = 121
arr[48] = 49
arr[41] = 95
arr[4] = 101
arr[40] = 111
arr[27] = 108
arr[26] = 102
arr[46] = 95
arr[35] = 65
arr[39] = 115
arr[28] = 64
arr[43] = 117
arr[16] = 95
arr[50] = 51
arr[15] = 117
arr[33] = 117
arr[23] = 77
arr[17] = 102
arr[25] = 95
for i in arr:
    print(chr(i),end="")
```


* Flag:

```
CTFlearn{w0w_you_f0und_My_fl@g_y0u_Ar3_so_much_n1c3}
```