# Rangoon!

## Description

* This is the third in a series of introductory Reversing Challenges; Reyjkavik, Riyadh and Rangoon. These are designed for people new to Reversing. A little gdb, C and Assembler knowledge should be enough to solve this challenge. Good Luck!
* [Attachement](https://ctflearn.com/challenge/download/994)

## Solution

1. Using `DIE` , we found it was ELF file. 

       Rangoon: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=2d383d91796b6febac3818ae69bc5191723c695e, for GNU/Linux 3.2.0, not stripped

2. Using  `IDA64` to analys file



![Imgur](https://i.imgur.com/zkcYz3h.png)

![Imgur](https://i.imgur.com/hn0VegR.png)

Hàm `FillInStrings` tạo mảng `strings` 16 phần tử và lưu các chuỗi vào từng phần tử

![Imgur](https://i.imgur.com/wEEQKCr.png)

Kiểm tra 9 kí tự đầu của tham số `input_value` có là `"CTFlearn{"` và phần tử cuối là có `"}"`, phần tử 17 và 22 có là `"_"` => giá trị của `v8=3` và `v9=1` và `v7=12` => `v12=strings[3]` và  `v14=string[8]` và `v15=string[12]` tức là `Princess` và `Maha` và `Devi`

Tạo mảng `buffer` để lưu giá trị để `strcmp` với `input_value` - nó sẽ là `flag`. Nạp dữ liệu vừa tìm được vào chuỗi ta có được flag


* Flag:

```
CTFlearn{Princess_Maha_Devi}
```