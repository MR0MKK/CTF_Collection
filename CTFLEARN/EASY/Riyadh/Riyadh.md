# Riyadh!

## Description

* Another entry level Reversing challenge, if you are new to Reversing you probably want to try my Reyjkavik challenge before attempting this challenge. Good Luck! The flag is hidden inside the Riyadh program. Solve the Challenge, get the flag, and I have included the encrypted sources used to create the challenge in the Riyadh.zip file. If you do to the work of solving the Challenge, I'm providing the Challenge source code (C++ and Python) if you are interested in studying the sources after solving the challenge. I think this is a great way to improve your Reversing skills when learning. Please don't share the sources or flag after you solve the challenge.
* [Attachement](https://ctflearn.com/challenge/download/991)

## Solution

1. Using `DIE` , we found it was ELF file. 

       Riyadh: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=393ea266da40acda58b1102e4aa0433cbf87174e, for GNU/Linux 3.2.0, not stripped


2. Using  `IDA64` to analys file



![Imgur](https://i.imgur.com/Q0GYEIr.png)

![Imgur](https://i.imgur.com/QeRdT0N.png)

Thử thực thi chương trình ta được kết quả như sau:

![Imgur](https://i.imgur.com/kLzcsXO.png)

Quan sát trong `strings` ko có chuỗi nào trong các chuỗi in ra màn hình -> chuỗi được sinh ra trong các hàm `Msg`

Có hàm CTFLeanHiddenFlag() -> dự đoán `flag` được dấu trong này -> đặt breakpoint và quan sát

![Imgur](https://i.imgur.com/LjnR01i.png)

Hàm Msg3 đã sửa `buffer` thành `CTFlearn{Reversing_Is_Easy}` nhưng khi đến hàm Msg4 thì thành 

![Imgur](https://i.imgur.com/o3OtB39.png)


Nếu tiếp tục đọc ta thấy đề có yêu cầu ta nhập chuỗi độ dài 30 kí tự, thử nhập ` "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" ` 

Quan sát `buffer` ko còn khả năng được sử dụng để tạo `flag` nên ta thử kiểm tra biến `maybe_flag`. Hàm Msg5 xử lý biến `maybe_flag` sau đó `XOR buffer` nếu tất cả là 0 thì OK. Nên đặt breakpoints xem `maybe_flag` là gì!!

![Imgur](https://i.imgur.com/xxNmNnv.png)


* Flag:

```
CTFlearn{Masmak_Fortress_1865}
```