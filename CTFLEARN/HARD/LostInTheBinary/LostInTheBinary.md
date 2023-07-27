# Lost In The Binary!

## Description

* I lost a flag inside this binary, please help me to find it. If you trigger certain anti-debugging techniques, you might get false flags…. flag format: FLAG-(str)
* [Attachement](https://mega.nz/file/ifgzQQCC#E1W0cSOFRvi7bE_v419rzwQB2jAHF0IsIRAWL6H1RNE)

## Solution

1. Using `DIE` , we found it was ELF file.

    lost_in_bin: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 2.6.32, BuildID[sha1]=aad03a2370bd8a2fa018be22cf557b18621a61af, stripped

2. Dùng `IDA` để phân tích chương trình

![Imgur](https://i.imgur.com/jOr0V6f.png)

Cho người dùng nhập vào, yếu cầu 21 kí tự rồi tính toán, chả có gì cả!!!

```
key = "IdontKnowWhatsGoingOn"
str_list = [8, 0, 0, 0, 6, 0, 0, 0, 44, 0, 0, 0, 58, 0, 0, 0, 50, 0, 0, 0, 48, 0, 0, 0, 28, 0, 0, 0, 92, 0, 0, 0, 1, 0, 0, 0, 50, 0, 0, 0, 26, 0, 0, 0, 18, 0, 0, 0, 69, 0, 0, 0, 29, 0, 0, 0, 32, 0, 0, 0, 48, 0, 0, 0, 13, 0, 0, 0, 27, 0, 0, 0, 3, 0, 0, 0, 124, 0, 0, 0, 19, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
flag = ""

for i, char in enumerate(key):
    flag += chr(ord(char) ^ str_list[i*4])

print(flag)

```

* Flag:

```
AbCTF{r3vers1ng_dud3}
```

Đấy là code khi nào chứ lúc sau đọc lại nó hoàn toàn khác 

![Imgur](https://i.imgur.com/xEt7HnP.png)

Ta nhận thấy có sử dụng `ptrace-anti-debug`. Tại một thời điểm chỉ có một tiến trình `strace` được thực hiện, nhờ vậy ta có thể sử dụng gọi mã để phát hiện có đang `Debug`. Thông tin chi tiết và cách bypass ở [Link](https://seblau.github.io/posts/linux-anti-debugging)

Tên hàm rối mắt quá => đổi tên

![Imgur](https://i.imgur.com/pkbjzrt.png)

Bạn có thể dùng Casio cho nhanh, mình code cho các bạn có tiền mua laptop mà ko có để mua Casio. Hướng dẫn sử dụng z3: https://www.youtube.com/watch?v=BUhEKDmcGv0

```
from z3 import *

a = Int('a')	# qword_602148
b = Int('b')	# qword_602150
c = Int('c')	# qword_602158
d = Int('d')	# qword_602160

s = Solver()
s.add(-24 * a + (-18 * b) + (-15 * c) + (-12 * d) == -18393)
s.add(9 * c + 18 * (b + a) + -9 * d == 4419)
s.add( 4 * c + 16 * a + 12 * b + 2 * d == 7300)
s.add(-6 * (b + a) + -3 * c+ -11 * d == -8613)
print(s.check())
print(s.model())

#   [d = 510, a = 227, c = 317, b = 115]
```
* Flag:
```                                                                     
FLAG-21a84f2c7c7fd432edf1686215db05ea
```
