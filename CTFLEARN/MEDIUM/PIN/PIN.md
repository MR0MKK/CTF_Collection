# PIN!

## Description

* Can you crack my pin?
* [Attachement](https://mega.nz/#!PXYjCKCY!F2gcs83XD6RxjOR-FNWGQZpyvUFvDbuT-PTnqRhBPGQ)

## Solution

1. Using `DIE` , we found it was ELF file.


        rev1: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 2.6.32, BuildID[sha1]=c5f9af621b132c2028d8e689cbb5b707f3f3cd28, not stripped
    

2. Dùng `IDA` để phân tích chương trình

![Imgur](https://i.imgur.com/5H44o3W.png)

![Imgur](https://i.imgur.com/ghU4vrL.png)

Chỉ cần nhập mã Pin là `333333` là xong

* Flag:

```
CTFlearn{333333}
```