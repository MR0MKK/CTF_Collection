# Ramada!

## Description

* This is a beginners Reversing Challenge. It is build with the optimization level set to 0 so that the assembler is more readable. If you are new to reversing, please remember that to solve Reversing challenges you probably need to know some C/C++, Assembler and also some experience with gdb (the gnu debugger). And maybe Ghidra
* [Attachement](https://ctflearn.com/challenge/download/1009)

## Solution

1. Using `DIE` , we found it was ELF file. 

       ramada: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=dd929c5a5dc32ca304cdbb781e14438d09f036b6, for GNU/Linux 3.2.0, not stripped

2. Using  `IDA64` to analys file



![Imgur](https://i.imgur.com/HRUmq91.png)


Hàm `FillInStrings` tạo mảng `strings` 16 phần tử và lưu các chuỗi vào từng phần tử

![Imgur](https://i.imgur.com/wEEQKCr.png)

Kiểm tra 9 kí tự đầu của tham số `input_value` có là `"CTFlearn{"` và phần tử cuối là có `"}"`. Tham số gồm 31 kí tự 

Tạo mảng `buffer` để lưu giá trị để `strcmp` với `input_value` - nó sẽ là `flag`. Nạp dữ liệu vừa tìm được vào chuỗi ta có được flag


![Imgur](https://i.imgur.com/j7ZOkj8.png)

Hàm `CheckFlag` kiểm tra `input_value[i] == input_value[i] * input_value[i] * input[i]`
```
import numpy as np
key = [0x13693, 0x6b2c0, 0x11a9f9, 0x157000, 0x1cb91, 0x1bb528, 0x1bb528, 0xded21, 0x144f38, 0xfb89d, 0x169b48, 0xd151f, 0x8b98b, 0x17d140, 0xded21, 0x1338c0, 0x1338c0, 0x11a9f9, 0x1b000, 0x144f38, 0x1734eb]
flag = ""
for d in key:
	i = round(np.cbrt(d))
	flag+=chr(i)
print(flag)
```
* Flag:

```
CTFlearn{+Lip1zzaner_Stalli0ns}
```