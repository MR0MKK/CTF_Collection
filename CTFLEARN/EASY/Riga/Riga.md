# Riga!

## Description

* Riga is another beginner Reverse Engineering Challenge. Ghidra is a good tool to get started with disassembly and some RE challenges can be solved using Ghidra alone (no gdb required). The sources are included as sources.zip.enc... solve the challenge, get the flag, view the sources used to create the challenge if you are interested. Good Luck!
* [Attachement](https://ctflearn.com/challenge/download/996)

## Solution

1. Using `DIE` , we found it was ELF file. 

       riga: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=2c803359d6379e9170a157cb708164d5e09a4a70, for GNU/Linux 3.2.0, not stripped

2. Using  `IDA64` to analys file

![Imgur](https://i.imgur.com/qbC2NxG.png)

Hàm `SteredSaurekauto0()` để in ra chuỗi `Welcome to the CTFLearn.com Riga Reversing Challenge!` và `SteredSaurekauto1()` để in ra chuỗi `Usage: Riga flag`.

Chương trình thực hiện lưu tham số truyền vào `buffer`. Thực hiện `XOR` với `0xDE` nhưng chả quan trọng đâu vì lát nữa lại `XOR` với `0xDE` về giá trị ban đầu.

Đọc code và thực hiện dịch ngược để tìm flag

```
pickles0 = [159, 174, 156, 182, 189, 185, 239, 235, 230, 158, 185, 236, 179, 185, 227, 185, 187, 168, 137, 227, 189, 239, 187, 150, 185, 237, 227, 137, 185, 228]
pickles1 = [158, 173, 147, 181, 188, 184, 238, 234, 229, 144, 186, 184, 235, 186, 237, 227, 232, 188, 238, 186, 237, 235, 184, 238, 236, 251]
pickles2 = [157, 172, 146, 235, 179, 191, 237, 233, 228, 151, 185, 148, 232, 225, 179, 185, 148, 191, 227, 225, 183, 191, 255, 250]

def function0():
    s = ['' for _ in range(len(pickles0))]
    for i in range(len(pickles0)):
        value = pickles0[i] ^ 0xCB
        if (value + 95) < 150:
            s[i] = chr(value + 78)
        else:
            s[i] = chr(value - 17)

    print(''.join(s))

def function1():
    s = ['' for _ in range(len(pickles1))]
    for i in range(len(pickles1)):
        value = pickles1[i] ^ 0xCB
        if (value + 95) < 150:
            s[i] = chr(value + 77)
        else:
            s[i] = chr(value - 18)

    print(''.join(s))

def function2():
    s = ['' for _ in range(len(pickles2))]

    for i in range(len(pickles2)):
        value = pickles2[i] ^ 0xCB
        if (value + 95) < 150:
            s[i] = chr(value + 76)
        else:
            s[i] = chr(value - 19)

    print(''.join(s))
function0() 
function1()
function2()
```


* Flag:

```
CTFlearn{Daugava_R1ver_Latv1a}
CTFlearn{I_am_super_smart}
CTFlearn{I_Love_Latvia}
```