# Reykjavik!

## Description

* Good beginning Reversing challenge - jump into gdb and start looking for the flag!
* [Attachement](https://ctflearn.com/challenge/download/990)

## Solution

1. Using `DIE` , we found it was ELF file. 

![Imgur](https://i.imgur.com/vcSnGCO.png)

2. Using  `IDA64` to analys file

![Imgur](https://i.imgur.com/9zCXiyI.png)

Đề bài cho phép ta truyền tham số khi thực hiện chương trình, tham số này lưu vào `v3` vào để cmp với chuỗi dữ liệu được tạo từ chương trình. 

Có thể dùng dùng `Watch View` để khi `Debug` có thể xem giá trị tại địa chỉ `v6` thay đổi nhưng tôi ko thích nên viết chương trình giải mã

```
key = [0xE8, 0xFF, 0xED, 0xC7, 0xCE, 0xCA, 0xD9, 0xC5, 0xD0, 0xEE,
       0xD2, 0xCE, 0xF4, 0xE7, 0x9B, 0xDD, 0xCE, 0xF4, 0xE2, 0xC8,
       0xCE, 0xC7, 0xCA, 0xC5, 0xCF, 0xF4, 0xD6]

flag = ''.join(chr(i ^ 0xAB) for i in key)

print("Flag:", flag)

```

* Flag:

```
CTFlearn{Eye_L0ve_Iceland_}
```