# ReverseMe!

## Description

* A simple reverse engineering challenge.
* [Attachement](https://ctflearn.com/challenge/download/989)

## Solution

1. Using `DIE` , we found it was ELF file.


        reverseme: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=82b8c684b10370209f59cd974c59a104e1f9a436, not stripped
    

2. Dùng `IDA` để phân tích chương trình

![Imgur](https://i.imgur.com/ZJRf679.png)

Không hiểu vì sao IDA làm mất một vài số nhưng ko sao cả, nó vẫn dễ. Đọc một tí là ra!!! 

```

cmp_value = [87, 66, 75, 69, 204, 187, 129, 204, 113, 122, 113, 102, 223, 187, 134, 205, 100, 111, 110, 92, 242, 173, 154, 216, 126, 111]
xor_value = [1, 3, 3, 7, 222, 173, 190, 239]
flag = ""
def swapPositions(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list

for i in range(0,len(cmp_value),2):
    swapPositions(cmp_value,i,i+1)

for i in range(len(cmp_value)):
    flag += chr(cmp_value[i] ^ xor_value[i%(len(xor_value))])

print(flag)

```

* Flag:

```
CTFLearn{reversing_is_fun}
```