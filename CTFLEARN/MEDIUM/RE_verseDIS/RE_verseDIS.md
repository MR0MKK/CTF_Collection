# RE_verseDIS!

## Description

* Could you find the hidden password?
* [Attachement](https://mega.nz/#!XOwVmCSC!ut_5r6b32j2kD6EvlvsvJhmm58pbswusUXF08yI93Zo)

## Solution

1. Using `DIE` , we found it was ELF file.


        problem: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 2.6.32, BuildID[sha1]=c01b7ec3bec0b0c2eb73b2c8fdbfea602009384d, not stripped
    

2. Dùng `IDA` để phân tích chương trình

![Imgur](https://i.imgur.com/h8Hoh4C.png)

Chả có gì cả, dịch ngược tí là xong 

```

key = "IdontKnowWhatsGoingOn"
msg = [8,0,0,0,6,0,0,0,44,0, 0,0,58,0,0,0,50,0,0,0, 48,0,0,0,28,0,0,0,92,0, 0,0,1,0,0,0,50,0,0,0, 26,0,0,0,18,0,0,0,69,0, 0,0,29,0,0,0,32,0,0,0, 48,0,0,0,13,0,0,0,27,0, 0,0,3,0,0,0, 124,0,0,0, 19,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0]
flag = "".join(chr(ord(key[i])^msg[i*4]) for i in range(len(key)))
print(flag)

```

* Flag:

```
AbCTF{r3vers1ng_dud3}
```