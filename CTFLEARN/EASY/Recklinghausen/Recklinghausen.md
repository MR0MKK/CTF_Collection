# Recklinghausen!

## Description

* Once you solve the challenge you can use the flag to decrypt the souces.zip.enc file provided, if you are interested in seeing the source programs used to create the challenge.
* [Attachement](https://ctflearn.com/challenge/download/995)

## Solution

1. Using `DIE` , we found it was ELF file. 

       Recklinghausen: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=3b8314899279e773a26ed87ff7201fd4cb95e732, for GNU/Linux 3.2.0, not stripped

2. Using  `IDA64` to analys file



![Imgur](https://i.imgur.com/V9nn0TN.png)

![Imgur](https://i.imgur.com/hYZXDPo.png)

Hàm `CheckMsg` kiểm tra `data[i] == 0X7E ^ input_value[i]`

![Imgur](https://i.imgur.com/xW6MGHr.png)


```
key = [61, 42, 56, 18, 27, 31, 12, 16, 5, 44, 11, 22, 12, 24, 27, 13, 10, 13, 14, 23, 27, 18, 27, 33, 56, 27, 13, 10, 23, 8, 31, 18, 3]
flag = "".join(chr(i ^ 0x7E) for i in key)
print(flag)

```
* Flag:

```
CTFlearn{Ruhrfestspiele_Festival}```