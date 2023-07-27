# PIN!

## Description

* Some versions of Ubuntu do not ship with 32 bit libraries for gcc. If you can't run the Rio32 program, instructions are included in the readme to install the package you probably need. If you run angr on the Rio32 exe, please leave a comment indicating if angr could find the flag.
* [Attachement](https://ctflearn.com/challenge/download/1015)

## Solution

1. Using `DIE` , we found it was ELF file.

        rio32: ELF 32-bit LSB pie executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, BuildID[sha1]=9aa672f9274ea8de2eec21b3b66029ade75dc3fb, for GNU/Linux 3.2.0, not stripped
    
2. Dùng `IDA` để phân tích chương trình

![Imgur](https://i.imgur.com/qNg5ksC.png)

![Imgur](https://i.imgur.com/OXSogR4.png)

Chương trình yêu cầu ta truyền 2 tham số. Hàm `GetArgs` kiểm tra các giá trị truyền vào có giá trị từ 0-9. Kiểm tra 2 giá trị có tổng là 20 hoặc tích là 100, nếu đúng thì tính toán in ra flag.

Hàm `InitData` nhìn khủng kiếp nhưng chả cần phân tích đâu. Ta patch để nó cho phép ta truyền các số có 2 kí tự => ta nhập 2 số là 10 => ra flag

* Flag:

```
CTFlearn{+123R10..de..JaneiR0}
```