# Salty!

## Description

* I like my hashes salty. Like, REALLY salty.
* [Attachement](https://imaginaryctf.org/r/FB146915)

## Solution
Chương trình cho ta nhập `command` để kết hợp với `salt` tạo `hash sha512`, so sánh với giá trị được tính toán. Dùng https://10015.io/tools/sha512-encrypt-decrypt để tìm ra giá trị nhập vào là `water`. Ta có được đường dẫn https://pastebin.com/vU76aJvC. Nhập `water` và được flag


* Flag:
```
ictf{s4lty_w4ter_1nd33d_4f285a3}
```